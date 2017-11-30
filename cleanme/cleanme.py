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
from video import Video
from managefiles import ManageFiles
from workers import Worker


video = Video()
data_files = ManageFiles()
worker = Worker()

"""

def sorting_video_files(path,files,path_dest=None):

	global folder_title


	main function to sort video files

	if the video files is a TV serie, the function check if a directory already exist to store it inside,
	if not create a specifique one with the file name and its season

	if the video files is a movie, function check if a directory already exist to store it inside,
	if not create a specifique one only for movies

	furthermore, the fonction take into account if the file is a folder or file with his extension

	def sorting_video_files(path,file_name,file_extension=None,path_dest=None):



	data_files.split_files(files)

	filename = data_files.filename
	file_extension = data_files.file_extension


	video.extract_metadata(files)


	if path_dest != None:

		if video.is_video:

			if video.is_serie:

				folder_title = "/" + video.title + "_season_" + str(video.season)
				specific_series_folder = path_dest + folder_title

				if data_files.file_extension != None:

					if os.path.exists(specific_series_folder):
						shutil.move(path + "/" + files, specific_series_folder + "/" + files)
					else:
						os.mkdir(specific_series_folder)
						shutil.move(path + "/" + files, specific_series_folder + "/" + files)

				else:
					if os.path.exists(specific_series_folder):
						shutil.move(path + "/" + filename, specific_series_folder + "/" + filename)
					else:
						os.mkdir(specific_series_folder)
						shutil.move(path + "/" + filename, specific_series_folder + "/" + filename)
			else:

				folder_title = "/divers_movies"
				divers_movies_folder = path_dest + folder_title

				if data_files.file_extension != None:
					if os.path.exists(divers_movies_folder):
						shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
					else:
						os.mkdir(divers_movies_folder)
						shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
				else:
					if os.path.exists(divers_movies_folder):
						shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)
					else:
						os.mkdir(divers_movies_folder)
						shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)
	else:

		if video.is_video:

			if video.is_serie:

				specific_series_folder = path + "/" + video.title + "_season_" + str(video.season)

				if data_files.file_extension != None:

					if os.path.exists(specific_series_folder):
						shutil.move(path + "/" + files, specific_series_folder + "/" + files)
					else:
						os.mkdir(specific_series_folder)
						shutil.move(path + "/" + files, specific_series_folder + "/" + files)
				else:
					if os.path.exists(specific_series_folder):
						shutil.move(path + "/" + filename, specific_series_folder + "/" + filename)
					else:
						os.mkdir(specific_series_folder)
						shutil.move(path + "/" + filename, specific_series_folder + "/" + filename)
			else:


				divers_movies_folder = path + "/divers_movies"

				if data_files.file_extension != None:

					if os.path.exists(divers_movies_folder):
						shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
					else:
						os.mkdir(divers_movies_folder)
						shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
				else:

					if os.path.exists(divers_movies_folder):
						shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)
					else:
						os.mkdir(divers_movies_folder)
						shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)

"""

"""
def manage_data_video(path,path_dest=None):


	main function which initiate video metadata analysis, extract metadata, sorting according metadata


	global list_video_files

	list_video_files = []


	list_files = data_files.list_files(path)

	i = 0
	while i <= len(data_files.list_files(path)):

		for files in list_files:

			if video.check(path,files):

				list_video_files.append(files)

				if path_dest != None:

					#sorting_video_files(path,files,path_dest)
					worker.files_sorting()

				else:

					sorting_video_files(path,files)


		bar.update(i)

		i += 1
	print(list_video_files)
	bar.finish()

"""


def main():

	"""
	main function to launch the script

	"""

	global bar
	global path
	global filename
	global file_extension


	bar = progressbar.ProgressBar(
	widgets=[progressbar.Bar('#','[',']'),progressbar.Percentage()]
	)


	parser = argparse.ArgumentParser(description=" cleanme is a python script to clean a garbage directory, like your download directory")
	parser.add_argument('-p','--path', action="store",help=" Enter the path of the directory to be cleaned",type=str,default="")
	parser.add_argument('-d','--destination',action='store',help=" Use -d to specify a path directory to copy cleaned data",type=str,default="")

	args = parser.parse_args()

	try:

		path = args.path

		if not args.destination:

			print(" -> Starting script for video files only ...")


			worker.files_deduplication(path)

			print("NB duplicate : " + str(worker.count_duplicate))

			time.sleep(5)

			worker.files_sorting(path)

			print("NB video file managed after deduplication " + str(worker.count_video_files))

			#manage_data_video(path)


			#print(str(len(list_video_files)) +  " Video files managed ")

		elif args.destination:

			path_dest = args.destination

			print(" -> Starting script for vide files with a specific destination")

			manage_data_video(path,path_dest)

			print(str(len(list_video_files)) +  " Video files managed ")

	except FileNotFoundError as e:
		print("Wrong or no path specified, detailed error : " + str(e))

if __name__ == '__main__':
	main()
