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



class Worker:

    def __init__(self):
        self.files_duplicate = None


    def deduplication(self,path):

        Files = ManageFiles()
        video = Video()

        files = Files.list_files(path)


        i1 = 0

        files_number = (len(files)-1)

        while i1 < files_number:

            if video.check(path,files[i1]):

            #print(video.extract_metadata(files[i1]))
            #print(video.extract_metadata(files[i1])["type"]["serie"][6]["language"])

                serie_status_1 = video.extract_metadata(files[i1])["type"]["serie"][0]["status"]
                serie_title_1 = video.extract_metadata(files[i1])["type"]["serie"][1]["title"]
                serie_season_1 = video.extract_metadata(files[i1])["type"]["serie"][2]["season"]
                serie_episode_1 = video.extract_metadata(files[i1])["type"]["serie"][3]["episode"]
                serie_resolution_1 = video.extract_metadata(files[i1])["type"]["serie"][5]["resolution"]
                serie_language_1 = video.extract_metadata(files[i1])["type"]["serie"][6]["language"]


                i2 = i1 + 1

                while i2 <= files_number:

                    serie_status_2 = video.extract_metadata(files[i2])["type"]["serie"][0]["status"]
                    serie_title_2 = video.extract_metadata(files[i2])["type"]["serie"][1]["title"]
                    serie_season_2 = video.extract_metadata(files[i2])["type"]["serie"][2]["season"]
                    serie_episode_2 = video.extract_metadata(files[i2])["type"]["serie"][3]["episode"]
                    serie_resolution_2 = video.extract_metadata(files[i2])["type"]["serie"][5]["resolution"]
                    serie_language_2 = video.extract_metadata(files[i2])["type"]["serie"][6]["language"]

                    if serie_title_1 == serie_title_2:
                        if serie_season_1 == serie_season_2:
                            if serie_episode_1 == serie_episode_2:
                                if serie_resolution_1 != None and serie_resolution_2 != None:
                                    if serie_resolution_1 == serie_resolution_2:
                                        print("ligne 66 " + files[i1] + files[i2])
                                        #os.remove(path + "/" + files[i2])
                                        #files_number -= 1
                                    elif serie_resolution_1 == "1080p" and serie_resolution_2 == "720p":
                                        print("ligne 69 " + files[i1] + files[i2])




                                #print("duplicate")

                                #files_number -= 1

                    i2 += 1
            i1 += 1
