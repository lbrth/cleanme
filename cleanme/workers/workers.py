#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import os.path
import shutil
from video.video import Video
from managefiles.managefiles import ManageFiles



class Worker:

    """ Class with the two main algorithme :
        - Algorithme to perform a deduplication task
        - Algorithme to sort and clean files"""

    def __init__(self):
        self.files_duplicate = None
        self.count_duplicate = 0
        self.count_video_files = 0


    def files_deduplication(self, path):

        """ Deduplication algorithm for video files"""

        def files_deletion(path, files):

            deep_path = path + "/" + files

            if os.path.isdir(deep_path):
                shutil.rmtree(deep_path)
            else:
                os.remove(deep_path)


        def deduplication_resolution(file_resolution_1, file_resolution_2, files_number):

            """ Local algorithm of deduplication for video resolution """

            if file_resolution_1 != None and file_resolution_2 != None:
                if file_resolution_1 == file_resolution_2:
                    files_deletion(path, files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "1080p" and file_resolution_2 == "720p":
                    files_deletion(path, files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "720p" and file_resolution_2 == "1080p":
                    files_deletion(path, files[i1])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "720p" and file_resolution_2 == "480p":
                    files_deletion(path, files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "480p" and file_resolution_2 == "720p":
                    files_deletion(path, files[i1])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "480p" and file_resolution_2 == "1080p":
                    files_deletion(path, files[i1])
                    self.count_duplicate += 1
                    files_number -= 1
                elif file_resolution_1 == "1080p" and file_resolution_2 == "480p":
                    files_deletion(path, files[i2])
                    self.count_duplicate += 1
                    files_number -= 1
            elif file_resolution_1 == "720p" and file_resolution_2 == None:
                files_deletion(path, files[i2])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == "1080p" and file_resolution_2 == None:
                files_deletion(path, files[i2])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == "480p" and file_resolution_2 == None:
                files_deletion(path, files[i2])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == "720p":
                files_deletion(path, files[i1])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == "1080p":
                files_deletion(path, files[i1])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == "480p":
                files_deletion(path, files[i1])
                self.count_duplicate += 1
                files_number -= 1
            elif file_resolution_1 == None and file_resolution_2 == None:
                files_deletion(path,files[i2])
                self.count_duplicate += 1
                files_number -= 1

        Files = ManageFiles()
        video = Video()

        files = Files.list_files(path)

        i1 = 0

        files_number = (len(files)-1)

        while i1 < files_number:

            if video.check(path,files[i1]):

                serie_title_1 = video.extract_metadata(files[i1])["type"]["serie"][1]["title"]
                serie_season_1 = video.extract_metadata(files[i1])["type"]["serie"][2]["season"]
                serie_episode_1 = video.extract_metadata(files[i1])["type"]["serie"][3]["episode"]
                serie_resolution_1 = video.extract_metadata(files[i1])["type"]["serie"][5]["resolution"]

                film_title_1 = video.extract_metadata(files[i1])["type"]["film"][1]["title"]
                film_resolution_1 = video.extract_metadata(files[i1])["type"]["film"][3]["resolution"]

                if video.is_serie:

                    i2 = i1 + 1

                    while i2 <= files_number:

                        serie_title_2 = video.extract_metadata(files[i2])["type"]["serie"][1]["title"]
                        serie_season_2 = video.extract_metadata(files[i2])["type"]["serie"][2]["season"]
                        serie_episode_2 = video.extract_metadata(files[i2])["type"]["serie"][3]["episode"]
                        serie_resolution_2 = video.extract_metadata(files[i2])["type"]["serie"][5]["resolution"]

                        if serie_title_1 == serie_title_2:
                            if serie_season_1 == serie_season_2:
                                if serie_episode_1 == serie_episode_2:
                                    deduplication_resolution(serie_resolution_1, serie_resolution_2, files_number)

                        i2 += 1

                else:

                    i2 = i1 + 1

                    while i2 <= files_number:

                        film_title_2 = video.extract_metadata(files[i2])["type"]["film"][1]["title"]
                        film_resolution_2 = video.extract_metadata(files[i2])["type"]["film"][3]["resolution"]

                        if film_title_1 == film_title_2:
                            deduplication_resolution(film_resolution_1,film_resolution_2,files_number)

                        i2 += 1

            i1 += 1

    def files_sorting(self, path, path_dest=None):

        """ Algorithm to clean and sort video files """

        def moving_to(path, specific_series_folder, main_serie_folder, files, path_dest=None):

            if path_dest != None:
                if os.path.exists(path_dest + specific_series_folder):
                    if os.path.exists(path_dest + main_serie_folder + specific_series_folder):
                        if not data_files.list_files(path_dest + specific_series_folder):
                            shutil.rmtree(path_dest + specific_series_folder)
                        else:
                            if os.path.exists(path + specific_series_folder):
                                if not data_files.list_files(path + specific_series_folder):
                                    shutil.rmtree(path + specific_series_folder)
                                else:
                                    shutil.move(path + specific_series_folder, path_dest + main_serie_folder)
                                    shutil.move(path + files, path_dest + main_serie_folder + specific_series_folder)
                                    self.count_video_files += 1
                            else:
                                shutil.move(path + files, path_dest + main_serie_folder + specific_series_folder)
                                self.count_video_files += 1
                    else:
                        if not data_files.list_files(path_dest + specific_series_folder):
                            shutil.rmtree(path_dest + specific_series_folder)
                        else:
                            shutil.move(path + files, path_dest + specific_series_folder)
                            shutil.move(path_dest + specific_series_folder, path_dest + main_serie_folder)
                            self.count_video_files += 1
                else:
                    if os.path.exists(path_dest + main_serie_folder + specific_series_folder):
                        if os.path.exists(path + specific_series_folder):
                            if not data_files.list_files(path + specific_series_folder):
                                shutil.rmtree(path + specific_series_folder)
                            else:
                                shutil.move(path + specific_series_folder, path_dest + main_serie_folder)
                                shutil.move(path + files, path_dest + main_serie_folder + specific_series_folder)
                                self.count_video_files += 1
                        else:
                            shutil.move(path + files, path_dest + main_serie_folder + specific_series_folder)
                            self.count_video_files += 1
                    else:
                        if os.path.exists(path + specific_series_folder):
                            if not data_files.list_files(path + specific_series_folder):
                                shutil.rmtree(path + specific_series_folder)
                            else:
                                shutil.move(path + specific_series_folder, path_dest + main_serie_folder)
                                shutil.move(path + files, path_dest + main_serie_folder + specific_series_folder)
                                self.count_video_files += 1
                        else:
                            os.mkdir(path_dest + main_serie_folder + specific_series_folder)
                            shutil.move(path + files, path_dest + main_serie_folder + specific_series_folder)
                            self.count_video_files += 1
            else:
                if os.path.exists(path + specific_series_folder):
                    if os.path.exists(path + main_serie_folder + specific_series_folder):
                        if not data_files.list_files(path + specific_series_folder):
                            shutil.rmtree(path + specific_series_folder)
                        else:
                            shutil.move(path + specific_series_folder, path + main_serie_folder)
                            shutil.move(path + files, path + main_serie_folder + specific_series_folder)
                            self.count_video_files += 1
                    else:
                        if not data_files.list_files(path + specific_series_folder):
                            shutil.rmtree(path + specific_series_folder)
                        else:
                            shutil.move(path + files, path + specific_series_folder)
                            shutil.move(path + specific_series_folder, path + main_serie_folder + specific_series_folder)
                            self.count_video_files += 1
                else:
                    if os.path.exists(path + main_serie_folder + specific_series_folder):
                        shutil.move(path + files, path + main_serie_folder + specific_series_folder)
                        self.count_video_files += 1
                    else:
                        os.mkdir(path + main_serie_folder + specific_series_folder)
                        shutil.move(path + files, path + main_serie_folder + specific_series_folder)
                        self.count_video_files += 1


        data_files = ManageFiles()
        video = Video()

        list_files_in_dir = data_files.list_files(path)

        for files in list_files_in_dir:

            data_files.split_files(files)
            filename = data_files.filename

            if video.check(path,files):

                video.extract_metadata(files)

                if path_dest != None:

                    if video.is_video:

                        if video.is_serie:

                            specific_series_folder =  "/" + video.title + "_season_" + str(video.season)
                            main_serie_folder = "/Series"

                            if data_files.file_extension != None:

                                if os.path.exists(path_dest + main_serie_folder):
                                    moving_to(path,specific_series_folder,main_serie_folder,files,path_dest)
                                else:
                                    os.mkdir(path_dest + main_serie_folder)
                                    moving_to(path,specific_series_folder,main_serie_folder,files,path_dest)

                        else:
                            folder_title = "/Films"
                            divers_movies_folder = path_dest + folder_title

                            if data_files.file_extension != None:
                                if os.path.exists(divers_movies_folder):
                                    shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
                                    self.count_video_files += 1
                                else:
                                    os.mkdir(divers_movies_folder)
                                    shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
                                    self.count_video_files += 1
                            else:
                                if os.path.exists(divers_movies_folder):
                                    shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)
                                    self.count_video_files += 1
                                else:
                                    os.mkdir(divers_movies_folder)
                                    shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)
                                    self.count_video_files += 1
                else:

                    if video.is_video:

                        if video.is_serie:

                            specific_series_folder =  "/" + video.title + "_season_" + str(video.season)
                            main_serie_folder = "/Series"

                            if data_files.file_extension != None:


                                if os.path.exists(path + main_serie_folder):
                                    moving_to(path,specific_series_folder,main_serie_folder,files)
                                else:
                                    os.mkdir(path + main_serie_folder)
                                    moving_to(path,specific_series_folder,main_serie_folder,files)

                        else:

                            divers_movies_folder = path + "/Films"

                            if data_files.file_extension != None:

                                if os.path.exists(divers_movies_folder):
                                    shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
                                    self.count_video_files += 1
                                else:
                                    os.mkdir(divers_movies_folder)
                                    shutil.move(path + "/" + files, divers_movies_folder + "/" + files)
                                    self.count_video_files += 1
                            else:
                                if os.path.exists(divers_movies_folder):
                                    shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)
                                    self.count_video_files += 1
                                else:
                                    os.mkdir(divers_movies_folder)
                                    shutil.move(path + "/" + filename, divers_movies_folder + "/" + filename)
                                    self.count_video_files += 1
