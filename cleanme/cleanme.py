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


			for i in range(len(data_files.list_files(path))):
				worker.files_deduplication(path)
				bar.update(i)
			bar.finish()
			print("Nb duplicate : " + str(worker.count_duplicate))
			for i in range(len(data_files.list_files(path))):
				worker.files_sorting(path)
				bar.update(i)
			bar.finish()
			print("NB video file managed after deduplication " + str(worker.count_video_files))




		elif args.destination:

			path_dest = args.destination

			print(" -> Starting script for vide files with a specific destination")
			for i in range(len(data_files.list_files(path))):
				worker.files_deduplication(path)
				bar.update(i)
			bar.finish()
			print("Nb duplicate : " + str(worker.count_duplicate))
			for i in range(len(data_files.list_files(path))):
				worker.files_sorting(path,path_dest)
				bar.update(i)
			bar.finish()
			print("NB video file managed after deduplication " + str(worker.count_video_files))


	except FileNotFoundError as e:
		print("Wrong or no path specified, detailed error : " + str(e))

if __name__ == '__main__':
	main()
