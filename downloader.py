from pytube import YouTube

def on_progress(bytes_remaining):
	print(bytes_remaining)

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
		for x in streamAudio:
			if biggestAudio == None or x.filesize_kb > biggestAudio.filesize_kb:
				biggestAudio = x
		print("audio size(kb): " + str(biggestAudio.filesize_kb))
		audioPath = biggestAudio.download(filename_prefix = "audio_")
	videoPath = biggestVideo.download(filename_prefix = "video_")

	print(biggestVideo)
	print(biggestAudio)

getVideo("https://www.youtube.com/watch?v=tPZRdUnV2vg")
exit()