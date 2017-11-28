import PTN
import os
import os.path

class Video:

	def __init__(self):
		self.metadata_serie = None
		self.metadata_movie = None
		self.is_video = bool

	def extract_metadata(self,video_file):
		"""
		Function which extract video metadata, using PTN library
		Return the video type, 'TV show' or 'movie'

		"""
		metadata = PTN.parse(video_file)

		metadata_type = {}

		if 'season' in metadata.keys():
			metadata_type['serie'] = metadata
			self.metadata_serie = metadata_type 
			return self.metadata_serie
		else:
			metadata_type['movie'] =  metadata
			self.metadata_movie = metadata_type
			return self.metadata_movie

	def check_video_extension(filename):

		"""
		check if the extension is a video format

		"""

		deep_path = path + "/" + filename

		if os.path.isdir(deep_path):
			for files in list_files(deep_path):
				fileName,fileExtension = os.path.splitext(files)
				if fileExtension in video_format:
					return True
				else:
					return False
		else:
			fileName,fileExtension = os.path.splitext(filename)
			if fileExtension in video_format:
				return True
			else:
				return False

	def check(self,video_file):
		"""
		function which identify if files is a video files

		if normaly we use the file extension  to know if it's a video.

		what about folder containing video files ?

		this function use  dictionnary keys of the PTN library to know if it's a video or not

		"""

		metadata = PTN.parse(video_file)

		if 'codec' in metadata.keys():
			if 'resolution' in metadata.keys():
				if 'quality' in metadata.keys():
					self.is_video = True
					return self.is_video
			elif 'quality' in metadata.keys():
				self.is_video = True
				return self.is_video


		elif 'resolution' in metadata.keys():

			if check_video_extension(video_file):
				return True
			else:
				return False

		elif 'quality' in metadata.keys():

			if check_video_extension(video_file):
				return True
			else:
				return False
















path = "Torrent9.tv ] The.Walking.Dead.S08E04.SUBFRENCH.HDTV.XviD-ZT.avi alias 2"

video = Video()
if video.extract_metadata(path)["serie"]:
	print("c'est une serie")
else:
	print("c'est un film")


if video.check(path) == True:
	print("c'est une video")
else:
	print("ce n'est pas une video")



