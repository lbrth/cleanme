# cleanme

Cleanme is python script to clean a folder where video data (films and tv series) are randomly stored and could be as duplicate.

`v1.3.1`
Python Version  : 3.5

**Why I need this ?**

Simply because I wanna clean my destination folder  of all my downloads. My movies and Tv series are not stored efficiently, and with the time it's impossible to search something inside. So I coded this little script to win some time and learn python.

**What does this script do? ?**

Cleanme can detect if the file or the folder is a Tv serie or a film. If it's a Tv serie, the script create a specifique folder with the name and the season of serie like : `Silicon Valley_season_4` and put inside a specifique folder for series, named `Series`. If it's a film, the script create a folder named `Film`and store it inside. For both of them, the script check if the folder already exist, if exist, it move data inside.

Cleanme can also detect video duplicates in your folder. The algorithm of deduplication is based on video metadata, and make the difference between several video resolution (1080p,720p,480p) to keep the best one. 


**Project status : in progress**

Some enhancement are in progress to do same things but for music files and may be some other ideas.

**How to install ?**

After download, run `python setup.py install`. run it with `sudo` if there is some troublshouting during installation.

**How to use it ?**

It's a script using as command line tool with 3 main options for the moment.

```

usage: cleanme [-h] -p PATH [-wd] [-od] [-d DESTINATION]

Python script to clean video folder : Deduplication - TV Series are sort by name and season - Films are sort inside unique folder

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Enter the source path of the directory to be cleaned`
  -d DESTINATION, --destination DESTINATION
                        Use -d to specify a path directory to copy cleaned
                        data
  -wd, --with_deduplication        Use -wd to activate the deduplication feature with the
                         cleaning job
 -od, --only_deduplication       Use -od to activate only the deduplication feature
  
```

**Exemples**

```python3 cleanme -p /path/to/video/ -d /other/path/ -wd```
