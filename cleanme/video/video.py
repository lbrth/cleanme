#!/usr/bin/env python3
# -*- coding: utf8 -*-
import PTN
import os
import os.path
from managefiles.managefiles import ManageFiles

global video_format

video_format = [".mkv",".avi",".mp4",".AVI",".MKV","MP4"]

class Video:

	"""Class with two main methods :

	- extract metadata video
	- check if a file is a video file """


	def __init__(self):
		self.metadata_serie = None
		self.metadata_movie = None
		self.is_video = bool
		self.is_serie = bool
		self.is_movie = bool
		self.video_extension = None
		self.title = None
		self.season = None
		self.episode = None
		self.quality = None
		self.resolution = None
		self.language = None
		self.extension = None

	def extract_metadata(self, video_file):

		"""
		Function which extract video metadata, using PTN library
		Return the video type, 'TV show' or 'movie'

		"""
		metadata = PTN.parse(video_file)

		if 'season' in metadata.keys():

			self.is_serie = True
			self.is_movie = False
			self.title = metadata["title"]
			self.season = metadata["season"]
			try:
				self.episode = metadata["episode"]
			except KeyError:
				self.episode = None
			try:
				self.quality = metadata["quality"]
			except KeyError:
				self.quality = None
			try:
				self.resolution = metadata["resolution"]
			except KeyError:
				self.resolution = None
			try:
				self.language = metadata["excess"]
			except KeyError:
				self.language = None
			try:
				self.extension = metadata["container"]
			except KeyError:
				self.extension = None

			return {
			  "type": {
				"serie" : [
				  {"status" : self.is_serie},
				  {"title" : self.title},
				  {"season" : self.season},
				  {"episode" : self.episode},
				  {"quality" : self.quality},
				  {"resolution":self.resolution},
				  {"language" : self.language},
				  {"extension" : self.extension}
				],
				"film" : [
				  {"status" : self.is_movie},
				  {"title" : self.title},
				  {"quality" : self.quality},
				  {"resolution":self.resolution},
				  {"language" : self.language},
				  {"extension" :self.extension}
				]
			  }
			}

		else:

			self.is_serie = False
			self.is_movie = True
			self.title = metadata["title"]
			try:
				self.quality = metadata["quality"]
			except KeyError:
				self.quality = None
			try:
				self.resolution = metadata["resolution"]
			except KeyError:
				self.resolution = None
			try:
				self.language = metadata["excess"]
			except KeyError:
				self.language = None
			try:
				self.extension = metadata["container"]
			except KeyError:
				self.extension = None

			return {
			  "type": {
				"serie" : [
				  {"status" : self.is_serie },
				  {"title" : self.title},
				  {"season" : self.season},
				  {"episode" : self.episode},
				  {"quality" : self.quality},
				  {"resolution":self.resolution},
				  {"language" : self.language},
				  {"extension" : self.extension}
				],
				"film" : [
				  {"status" : self.is_movie},
				  {"title" : self.title},
				  {"quality" : self.quality},
				  {"resolution":self.resolution},
				  {"language" : self.language},
				  {"extension" :self.extension}
				]
			  }
			}



	def check(self, path, video_file):

		global file_extension

		"""
		function which identify if files is a video files

		if normaly we use the file extension  to know if it's a video.

		what about folder containing video files ?

		this function use  dictionnary keys of the PTN library to know if it's a video or not

		"""

		#too many lines of code, should be integrate as function
		metadata = PTN.parse(video_file)

		video_check = ManageFiles()
		self.video_extension = video_check.split_files(video_file)["file_extension"]

		if 'title' in metadata.keys():
			if 'codec' in metadata.keys():
				if 'resolution' in metadata.keys():
					if 'quality' in metadata.keys():
						self.is_video = True
						return self.is_video
				elif 'quality' in metadata.keys():
					self.is_video = True
					return self.is_video
			elif 'resolution' in metadata.keys():

				deep_path = path + "/" + video_file

				if os.path.isdir(deep_path):
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

			elif 'season' in metadata.keys():

				deep_path = path + "/" + video_file

				if os.path.isdir(deep_path):
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

			elif 'episode' in metadata.keys():

				deep_path = path + "/" + video_file

				if os.path.isdir(deep_path):
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
			else:
				self.is_video = False
				return self.is_video
