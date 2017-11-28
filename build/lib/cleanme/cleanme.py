#!/usr/bin/python
# -*- coding: utf8 -*-


import os
import os.path
import shutil
import PTN
import argparse
import progressbar
import time
import sys
import video
import managefiles


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

def file_type_is_video(filename):

	"""
	function which identify if files is a video files

	if normaly we use the file extension  to know if it's a video.

	what about folder containing video files ?

	this function use  dictionnary keys of the PTN library to know if it's a video or not

	"""

	metadata = PTN.parse(filename)

	if 'codec' in metadata.keys():
		if 'resolution' in metadata.keys():
			if 'quality' in metadata.keys():
				return True
		elif 'quality' in metadata.keys():
			return True

	elif 'resolution' in metadata.keys():

		if check_video_extension(filename):
			return True
		else:
			return False

	elif 'quality' in metadata.keys():

		if check_video_extension(filename):
			return True
		else:
			return False

def extract_video_metadata(filename):

	"""
	Function which extract video metadata, using PTN library
	Return the video type, 'TV show' or 'movie'

	"""
	metadata = PTN.parse(filename)

	metadata_type = {}

	if 'season' in metadata.keys():
		metadata_type['serie'] = metadata
		return metadata_type
	else:
		metadata_type['movie'] =  metadata
		return metadata_type

def list_files(path):
	"""
	basic function to list files in a specified directory
	"""
	listFile = os.listdir(path)
	return listFile

def split_file(files):
	"""
	function splitting file to get the filename and its extension
	"""
	fileName,fileExtension = os.path.splitext(files)
	return {0:fileName,1:fileExtension}

def sorting_video_files(path,files,path_dest=None):

	global folder_title

	"""
	main function to sort video files

	if the video files is a TV serie, the function check if a directory already exist to store it inside,
	if not create a specifique one with the file name and its season

	if the video files is a movie, function check if a directory already exist to store it inside,
	if not create a specifique one only for movies

	furthermore, the fonction take into account if the file is a folder or file with his extension

	def sorting_video_files(path,file_name,file_extension=None,path_dest=None):
	"""

	file_type = extract_video_metadata(files)

	fileName = split_file(files)[0]
	fileExtension = split_file(files)[1]

	if path_dest != None:

		try:

			folder_title = "/" + file_type['serie']['title'] + "_season_" + str(file_type['serie']['season'])
			specific_series_folder = path_dest + folder_title

			if fileExtension != None:

				if os.path.exists(specific_series_folder):
					shutil.move(path + "/" + files, specific_series_folder + "/" + files)
				else:
					os.mkdir(specific_series_folder)
					shutil.move(path + "/" + files, specific_series_folder + "/" + files)

			else:

				if os.path.exists(specific_series_folder):
					shutil.move(path + "/" + fileName, specific_series_folder + "/" + fileName)
				else:
					os.mkdir(specific_series_folder)
					shutil.move(path + "/" + fileName, specific_series_folder + "/" + fileName)

		except:

			folder_title = "/divers_movies"
			divers_movies_folder = path_dest + folder_title

			if fileExtension != None:
				if os.path.exists(divers_movies_folder):
					shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
				else:
					os.mkdir(divers_movies_folder)
					shutil.move(path + "/" + files, divers_movies_folder + "/" + files)

			else:

				if os.path.exists(divers_movies_folder):
					shutil.move(path + "/" + fileName, divers_movies_folder + "/" + fileName)
				else:
					os.mkdir(divers_movies_folder)
					shutil.move(path + "/" + fileName, divers_movies_folder + "/" + fileName)
	else:

		try:

			specific_series_folder = path + "/" + file_type['serie']['title'] + "_season_" + str(file_type['serie']['season'])

			if fileExtension != None:

				if os.path.exists(specific_series_folder):
					shutil.move(path + "/" + files, specific_series_folder + "/" + files)
				else:
					os.mkdir(specific_series_folder)
					shutil.move(path + "/" + files, specific_series_folder + "/" + files)

			else:

				if os.path.exists(specific_series_folder):
					shutil.move(path + "/" + fileName, specific_series_folder + "/" + fileName)
				else:
					os.mkdir(specific_series_folder)
					shutil.move(path + "/" + fileName, specific_series_folder + "/" + fileName)

		except:

			divers_movies_folder = path + "/divers_movies"

			if fileExtension != None:

				if os.path.exists(divers_movies_folder):
					shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
				else:
					os.mkdir(divers_movies_folder)
					shutil.move(path + "/" + files, divers_movies_folder + "/" + files)

			else:

				if os.path.exists(divers_movies_folder):
					shutil.move(path + "/" + fileName, divers_movies_folder + "/" + fileName)
				else:
					os.mkdir(divers_movies_folder)
					shutil.move(path + "/" + fileName, divers_movies_folder + "/" + fileName)

def manage_data_video(path,path_dest=None):

	"""
	main function which initiate video metadata analysis, extract metadata, sorting according metadata

	"""
	global list_video_files

	list_video_files = []


	i = 0
	while i <= len(list_files(path)):

		for files in list_files(path):

			if file_type_is_video(files):

				fileExtension = split_file(files)[1]

				list_video_files.append(files)

				if path_dest != None:

					if os.path.isdir(path + "/" + files):
						sorting_video_files(path,files,path_dest)
					else:
						if fileExtension in video_format:
							sorting_video_files(path,files,path_dest)

				else:
					if os.path.isdir(path + "/" + files):
						sorting_video_files(path,files)
					else:
						if fileExtension in video_format:
							sorting_video_files(path,files)

		bar.update(i)

		i += 1

	bar.finish()

def clean_bring_pdf_files(files,path,path_dest=None):

	"""
	function which manage pdf files

	"""

	if path_dest != None:

		pdf_folder = path_dest + "/divers_pdf_files"

		if os.path.exists(pdf_folder):
			shutil.move(path + "/" + files,
				pdf_folder + "/" + files )
		else:
			os.mkdir(pdf_folder)
			shutil.move(path + "/" + files,
				pdf_folder + "/" + files )

	else:

		pdf_folder = path + "/divers_pdf_files"

		if os.path.exists(pdf_folder):
			shutil.move(path + "/" + files,
				pdf_folder + "/" + files )
		else:
			os.mkdir(pdf_folder)
			shutil.move(path + "/" + files,
				pdf_folder + "/" + files )

def clean_bring_img_files(files,path,path_dest=None):

	"""
	function which manage img files

	"""

	if path_dest != None:

		img_folder = path_dest + "/divers_img_files"

		if os.path.exists(img_folder):
			shutil.move(path + "/" + files,
				img_folder + "/" + files)
		else:
			os.mkdir(img_folder)
			shutil.move(path + "/" + files,
				img_folder + "/" + files)

	else:

		img_folder = path + "/divers_img_files"

		if os.path.exists(img_folder):
			shutil.move(path + "/" + files,
				img_folder + "/" + files)
		else:
			os.mkdir(img_folder)
			shutil.move(path + "/" + files,
				img_folder + "/" + files)




def main():

	"""
	main function to launch the script

	"""

	global bar
	global video_format
	global img_format
	global path
	global fileName
	global fileExtension


	list_pdf_files = []
	list_img_files = []


	bar = progressbar.ProgressBar(
	widgets=[progressbar.Bar('#','[',']'),progressbar.Percentage()]
	)


	parser = argparse.ArgumentParser(description=" cleanme is a python script to clean a garbage directory, like your download directory")
	parser.add_argument('-p','--path', action="store",help=" Enter the path of the directory to be cleaned",type=str,default="")
	parser.add_argument('-d','--destination',action='store',help=" Use -d to specify a path directory to copy cleaned data",type=str,default="")
	parser.add_argument('-v','--onlyVideo', action="store_true",help=" Use -v to clean and sort only video files",default=False)

	args = parser.parse_args()
	img_format = ['.rgb','.gif','.pbm','.pgm','.ppm','.tiff','.rast','.xbm','.jpeg','.bmp','.png','.psd','.jpg']
	video_format = ['.mkv','.avi','.mp4','.AVI']


	try:

		path = args.path

		if args.onlyVideo and not args.destination:

			print(" -> Starting script for video files only ...")

			manage_data_video(path)

			print(str(len(list_video_files)) +  " Video files managed ")

		elif args.onlyVideo and args.destination:

			path_dest = args.destination

			print(" -> Starting script for vide files with a specific destination")

			manage_data_video(path,path_dest)

			print(str(len(list_video_files)) +  " Video files managed ")


		elif args.path and not args.destination:

			print(" -> Starting script for video, PDF and img files")

			manage_data_video(path)

			i = 0
			while i <= len(list_files(path)):

				for files in list_files(path):

					fileName = split_file(files)[0]
					fileExtension = split_file(files)[1]

					if fileExtension == ".pdf":

						list_pdf_files.append(fileName)

						clean_bring_pdf_files(files,path)

					if fileExtension in img_format:

						list_img_files.append(fileName)

						clean_bring_img_files(files,path)

				bar.update(i)
				i += 1
			bar.finish()

			print(str(len(list_video_files)) +  " Video files managed ")
			print(str(len(list_pdf_files)) + " PDF files managed ")
			print(str(len(list_img_files)) + " Images files managed ")

		elif args.path and args.destination:

			print(" -> Starting script for video, PDF and img files with a specific destination")

			path_dest = args.destination

			manage_data_video(path,path_dest)

			i = 0
			while i <= len(list_files(path)):

				for files in list_files(path):

					fileName = split_file(files)[0]
					fileExtension = split_file(files)[1]

					if fileExtension == ".pdf":

						list_pdf_files.append(fileName)

						clean_bring_pdf_files(files,path,path_dest)

					if fileExtension in img_format:

						list_img_files.append(fileName)

						clean_bring_img_files(files,path,path_dest)

				bar.update(i)
				i += 1
			bar.finish()
			print(str(len(list_video_files)) +  " Video files managed ")
			print(str(len(list_pdf_files)) + " PDF files managed ")
			print(str(len(list_img_files)) + " Images files managed ")



	except FileNotFoundError as e:
		print("Wrong or no path specified, detailed error : " + str(e))

if __name__ == '__main__':
	main()
