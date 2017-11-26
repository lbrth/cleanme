import PTN
import os
import os.path
from managefiles import ManageFiles

global video_format

video_format = [".mkv",".avi",".mp4",".AVI",".MKV","MP4"]

class Video:


	def __init__(self):
		self.metadata_serie = None
		self.metadata_movie = None
		self.is_video = bool
		self.video_extension = None

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
			print(self.metadata_serie)
			return self.metadata_serie
		else:
			metadata_type['movie'] =  metadata
			self.metadata_movie = metadata_type
			print(self.metadata_movie)
			return self.metadata_movie



	def check(self,path,video_file):
		"""
		function which identify if files is a video files

		if normaly we use the file extension  to know if it's a video.

		what about folder containing video files ?

		this function use  dictionnary keys of the PTN library to know if it's a video or not

		"""

		metadata = PTN.parse(video_file)

		video_check = ManageFiles()
		self.video_extension = video_check.split_files(video_file)["file_extension"]

		if 'codec' in metadata.keys():
			if 'resolution' in metadata.keys():
				if 'quality' in metadata.keys():
					self.is_video = True
					return self.is_video
			elif 'quality' in metadata.keys():
				self.is_video = True
				return self.is_video

		elif 'resolution' in metadata.keys():
			#print("line 67 " + video_file)

			deep_path = path + "/" + video_file

			if os.path.isdir(deep_path):
				#print("dossier video : " + video_file)
				for data in video_check.list_files(deep_path):
					self.video_extension = video_check.split_files(data)["file_extension"]
					if self.video_extension in video_format:
						self.is_video = True
						return self.is_video
					else:
						self.is_video = False
						return self.is_video

			elif self.video_extension != None:
				if self.video_extension in video_format:
					self.is_video = True
					return self.is_video
				else:
					self.is_video = False
					return self.is_video

		elif 'quality' in metadata.keys():

			deep_path = path + "/" + video_file

			if os.path.isdir(deep_path):
				#print("dossier video : " + video_file)
				for data in video_check.list_files(deep_path):
					self.video_extension = video_check.split_files(data)["file_extension"]
					if self.video_extension in video_format:
						self.is_video = True
						return self.is_video
					else:
						self.is_video = False
						return self.is_video

			elif self.video_extension != None:
				if self.video_extension in video_format:
					self.is_video = True
					return self.is_video
				else:
					self.is_video = False
					return self.is_video
