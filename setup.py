from setuptools import setup
import os
import cleanme


setup(
name = 'cleanme',
version = '0.1',
author = 'lbrth',
author_email = 'olivierlabarthe6@gmail.com',
packages = ['cleanme'],
description = 'Python scripts to clean folders - specifically the folders where your movies and TV series are randomly stored (like your download folder)',
install_requires = ['parse-torrent-name','progressbar2']
)
