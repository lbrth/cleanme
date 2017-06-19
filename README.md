# cleanme

Cleanme is python script to clean a folder where video data (movie and tv serie) are ramdomly stored.

**Why I need this ?**

Simply because I wanna clean my destination folder  of all my downloads. My movies and Tv series are not stored efficiently, and with the time it's impossible to search something inside. So I coded this little script to win some time and learn python.

**What does this script do? ?**

Cleanme detect if the file or the folder is a Tv serie or a movie. If it's a Tv serie (this feature is the most helpful), the script create a specifique folder with the name and the season of serie like : `Silicon Valley_season_4`. If it's a movie, the script create a folder named `divers_movies`and store it inside. For both of them, the script check if the folder already exist, if exist, it move data inside.

Cleanme detect also `img`and `pdf`files to store it in specific folder for both.


**Project status : in progress**

The main objective now is to test it (on other OS) and become most-code effective
Some enhancement are in progress to do same things but for music files and may be some other ideas.

**How to install ?**

After download, run `python setup.py install`.

**How to use it ?**

It's a script using as command line tool with 3 main options for the moment.

`usage: cleanme.py [-h] [-p PATH] [-d DESTINATION] [-v]``

`cleanme is a python script to clean a garbage directory, like your download`
`directory`

`optional arguments:``
  `-h, --help            show this help message and exit`
  `-p PATH, --path PATH  Enter the path of the directory to be cleaned`
  `-d DESTINATION, --destination DESTINATION`
                        `Use -d to specify a path directory to copy cleaned`
                        `data`
  `-v, --onlyvideo       Use -v to clean and sort only video files`
  
