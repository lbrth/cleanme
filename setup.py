#!/usr/bin/env python3
from setuptools import setup,find_packages



setup(
name = 'cleanme',
description = 'Python script to clean and deduplicate video files',
url = 'https://github.com/lbrth/cleanme',
version = '2.0',
author = 'Olivier Labarthe',
author_email = 'olivierlabarthe6@gmail.com',
packages=find_packages(),
license = 'LGPL',
entry_points = {
    'console_scripts': ['cleanme=cleanme.cleanme:main'],
},
install_requires = ['parse-torrent-name','progressbar2'],
)
