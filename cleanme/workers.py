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
        self.count_duplicate = 0


    def deduplication(self,path):


        def deduplication_resolution(file_resolution_1,file_resolution_2,files_number):
            if file_resolution_1 != None and file_resolution_2 != None:
                if file_resolution_1 == file_resolution_2:
                    os.remove(path + "/" + files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "1080p" and file_resolution_2 == "720p":
                    os.remove(path + "/" + files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "720p" and file_resolution_2 == "1080p":
                    os.remove(path + "/" + files[i1])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "720p" and file_resolution_2 == "480p":
                    os.remove(path + "/" + files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "480p" and file_resolution_2 == "720p":
                    os.remove(path + "/" + files[i1])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "480p" and file_resolution_2 == "1080p":
                    os.remove(path + "/" + files[i1])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "1080p" and file_resolution_2 == "480p":
                    os.remove(path + "/" + files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
            elif file_resolution_1 == "720p" and file_resolution_2 == None:
                os.remove(path + "/" + files[i2])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == "1080p" and file_resolution_2 == None:
                os.remove(path + "/" + files[i2])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == "480p" and file_resolution_2 == None:
                os.remove(path + "/" + files[i2])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == "720p":
                os.remove(path + "/" + files[i1])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == "1080p":
                os.remove(path + "/" + files[i1])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == "480p":
                os.remove(path + "/" + files[i1])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == None:
                os.remove(path + "/" + files[i2])
                self.count_duplicate += 1
                files_number -= 1

        Files = ManageFiles()
        video = Video()

        files = Files.list_files(path)

        i1 = 0

        files_number = (len(files)-1)

        while i1 < files_number:

            if video.check(path,files[i1]):

                #print(video.extract_metadata(files[i1]))

                serie_status_1 = video.extract_metadata(files[i1])["type"]["serie"][0]["status"]
                serie_title_1 = video.extract_metadata(files[i1])["type"]["serie"][1]["title"]
                serie_season_1 = video.extract_metadata(files[i1])["type"]["serie"][2]["season"]
                serie_episode_1 = video.extract_metadata(files[i1])["type"]["serie"][3]["episode"]
                serie_resolution_1 = video.extract_metadata(files[i1])["type"]["serie"][5]["resolution"]
                serie_language_1 = video.extract_metadata(files[i1])["type"]["serie"][6]["language"]

                film_status_1 = video.extract_metadata(files[i1])["type"]["film"][0]["status"]
                film_title_1 = video.extract_metadata(files[i1])["type"]["film"][1]["title"]
                film_resolution_1 = video.extract_metadata(files[i1])["type"]["film"][3]["resolution"]

                if video.is_serie:

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
                                    deduplication_resolution(serie_resolution_1,serie_resolution_2,files_number)

                        i2 += 1

                else:#film

                    i2 = i1 + 1

                    while i2 <= files_number:

                        film_status_2 = video.extract_metadata(files[i2])["type"]["film"][0]["status"]
                        film_title_2 = video.extract_metadata(files[i2])["type"]["film"][1]["title"]
                        film_resolution_2 = video.extract_metadata(files[i2])["type"]["film"][3]["resolution"]

                        if film_title_1 == film_title_2:
                            deduplication_resolution(film_resolution_1,film_resolution_2,files_number)

                        i2 += 1



            i1 += 1
