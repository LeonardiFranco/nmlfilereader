import re

SONG_RE = re.compile('<ENTRY><PRIMARYKEY TYPE=\"TRACK\" KEY=\"([A-Z])(:.*:)(.*)\"></PRIMARYKEY>')
EXTENDED_RE = re.compile('<EXTENDEDDATA DECK=\".\" DURATION=\".*\" EXTENDEDTYPE=\"HistoryData\" PLAYEDPUBLIC="([01])" STARTDATE=\".*\" STARTTIME=\"([0-9]+)\"></EXTENDEDDATA>')
FILE_RE = ".*\.nml$"
DIRECTORY = "history/"