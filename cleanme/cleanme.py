#!/usr/bin/python
# -*- coding: utf8 -*-

import argparse
import progressbar
import time
from video import Video
from managefiles import ManageFiles
from workers import Worker


def main():

	"""
	main function to launch the script

	"""
	data_files = ManageFiles()
	worker = Worker()


	bar = progressbar.ProgressBar(
	widgets=[progressbar.Bar('#','[',']'),progressbar.Percentage()]
	)


	parser = argparse.ArgumentParser(description=" cleanme is a python script to clean a garbage directory, like your download directory")
	parser.add_argument('-p','--path',action="store",help=" Enter the source path of the directory to be cleaned",type=str,required=True)
	parser.add_argument('-wd','--with_deduplication',action="store_true",help=" Use -wd to activate the deduplication feature with the cleaning job", default=False)
	parser.add_argument('-od','--only_deduplication',action="store_true",help=" Use -od to activate only the deduplication feature", default=False)
	parser.add_argument('-d','--destination',action='store',help=" Use -d to specify a path directory to copy cleaned data",type=str,default="")

	args = parser.parse_args()

	try:

		path = args.path

		if args.path and not args.with_deduplication and not args.destination and not args.only_deduplication :

			print("path only")

			print("Cleanme will start to cleaned up your video file directory in the path " + path)
			time.sleep(2)
			for i in range(len(data_files.list_files(path))):
				worker.files_sorting(path)
				bar.update(i)
			bar.finish()
			print("Job done. " + str(worker.count_video_files) + " video files managed" )

		elif args.path and args.destination and not args.with_deduplication:

			path_dest = args.destination

			print("Cleanme will start to cleaned up your video file directory in the path " + path + " \n and moved it to " + path_dest)
			time.sleep(2)
			for i in range(len(data_files.list_files(path))):
				worker.files_sorting(path, path_dest)
				bar.update(i)
			bar.finish()
			print("Job done. " + str(worker.count_video_files) + " video files managed" )

		elif args.path and args.with_deduplication and not args.destination:
			print("Cleame will start to deduplicate your video files and then start the job to cleaned up your video file directory in the path " + path)
			time.sleep(2)
			for i in range(len(data_files.list_files(path))):
				worker.files_deduplication(path)
				bar.update(i)
			bar.finish()
			print("Deduplication job done. " + str(worker.count_duplicate) + " video files deleted during deduplication")
			time.sleep(2)
			print("Cleanme will start now to cleaned up your video file directory")
			for i in range(len(data_files.list_files(path))):
				worker.files_sorting(path)
				bar.update(i)
			bar.finish()
			print("Job done. " + str(worker.count_video_files) + " video files managed" )

		elif args.path and args.with_deduplication and args.destination:
			path_dest = args.destination
			print("Cleame will start to deduplicate your video files and then start the job to cleaned up your video file directory in the path " + path)
			time.sleep(2)
			for i in range(len(data_files.list_files(path))):
				worker.files_deduplication(path)
				bar.update(i)
			bar.finish()
			print("Deduplication job done. " + str(worker.count_duplicate) + " video files deleted during deduplication")
			time.sleep(2)
			print("Cleanme will start now to cleaned up your video file directory in the path " + path + " and moved it to " + path_dest)
			time.sleep(2)
			for i in range(len(data_files.list_files(path))):
				worker.files_sorting(path, path_dest)
				bar.update(i)
			bar.finish()
			print("Job done. " + str(worker.count_video_files) + " video files managed" )

		elif args.path and args.only_deduplication and not args.with_deduplication and not args.destination:
			print("Cleame will start to deduplicate your video files in the path " + path)
			time.sleep(2)
			for i in range(len(data_files.list_files(path))):
				worker.files_deduplication(path)
				bar.update(i)
			bar.finish()
			print("Deduplication job done. " + str(worker.count_duplicate) + " video files deleted during deduplication")



	except FileNotFoundError as e:
		print("Wrong or no path specified, detailed error : " + str(e))

if __name__ == '__main__':
	main()
