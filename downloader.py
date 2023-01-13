from pytube import YouTube
import ffmpeg

def getVideo(link):
	biggestVideo = None
	biggestAudio = None

	yt = YouTube(link)
	streamVideo = yt.streams.filter(type="video")
	streamAudio = yt.streams.filter(type="audio")
	for x in streamVideo:
		if biggestVideo == None or x.filesize_kb > biggestVideo.filesize_kb:
			biggestVideo = x
	print("video size(kb): " + str(biggestVideo.filesize_kb))

	if biggestVideo.includes_audio_track == False:
		needsCombine = True
		for x in streamAudio:
			if biggestAudio == None or x.filesize_kb > biggestAudio.filesize_kb:
				biggestAudio = x
		print("audio size(kb): " + str(biggestAudio.filesize_kb))
		audioPath = biggestAudio.download(output_path = "temp/", filename_prefix = "audio_")
	videoPath = biggestVideo.download(output_path = "temp/", filename_prefix = "video_")

	if needsCombine == True:
		textlist = open("temp/list.txt")
		textlist.write("file \"" + str(videoPath) + "\"\n" + "file \"" + str(audioPath) + "\"")
		# input_video = ffmpeg.input(videoPath)
		# input_audio = ffmpeg.input(audioPath)
		(
			ffmpeg
			.input("temp/list.txt", format="concat", safe=0)
			.output("output/" + biggestVideo.default_filename, c="copy")
			.run()
		)
		# ffmpeg.concat(input_video, input_audio, v=1, a=1).output("output/" + biggestVideo.default_filename, c="copy").run()

getVideo("https://www.youtube.com/watch?v=tPZRdUnV2vg")
exit()