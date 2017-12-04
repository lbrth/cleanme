#!/usr/bin/python3
# -*- coding: utf8 -*-
import os
import os.path


class ManageFiles:

	"""class which manage files, with two methods :

		- List files in a directory
		- Extract the filename from the file extension"""


	def __init__(self):
		self.list_files_in_directory = list
		self.filename = None
		self.file_extension = None

	def list_files(self,path):
		"""
		basic function to list files in a specified directory
		"""
		self.list_files_in_directory = os.listdir(path)
		return self.list_files_in_directory

	def split_files(self,files):
		"""
		function splitting file to get the filename and its extension
		"""
		self.filename,self.file_extension = os.path.splitext(files)
		return {"filename":self.filename,"file_extension":self.file_extension}
