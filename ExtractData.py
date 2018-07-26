from GetFiles import *
from Constants import *

class Song(object):
	def __init__(self,name,path):
		self.name = name
		self.path = path

	def __hash__(self):
		return hash(self.name + self.path)

	def __str__(self):
		return self.name

	def __eq__(self,other):
		return self.name == other.name and self.path == other.path

def parseTime(time):
	time = int(time)
	hours = int(time / 3600)
	minutes = int((time / 60) % 60)
	seconds = time % 60
	return"{:02}:{:02}:{:02}".format(hours, minutes, seconds)

def parsePlayed(played):
	return bool(int(played))

def parsePath(path):
	return path.replace("&amp;","&").replace(":","")

def getSongs(file):
	songs = []
	file = DIRECTORY + file
	with open(file, encoding="UTF-8") as f:
		for line in f:
			s = re.search(SONG_RE, line)
			e = re.search(EXTENDED_RE, line)
			if s:
				vol = s[1]
				path = parsePath(s[2])
				name = parsePath(s[3])
				song = Song(name, vol+path)
				songs.append(song)
			elif e:
				played = parsePlayed(e[1])
				time = parseTime(e[2])
				songs[-1].isPlayed = played
				songs[-1].timePlayed = time
	return songs

def getSongsPlayed(file):
	songList = getSongs(file)
	return list(filter(lambda x: x.isPlayed, songList))

def tracklist(files):
	with open("tracklist.txt", encoding="UTF-8", mode="w") as fout:
		for file in files:		
			fout.write(file + "\n")
			songs = getSongsPlayed(file)
			for song in songs:
				fout.write("\n")
				fout.write(" ".join([str(song.timePlayed),  str(song)]))
			fout.write("\nCantidad de temas: {}".format(len(songs)))
			fout.write("\n\n")

def numberOfTimesPlayed(files):
	songsAndQuantity = {}
	songs = []
	for file in files:
		songs.extend(getSongsPlayed(file))
	for song in songs:
		songsAndQuantity[song] = songsAndQuantity.get(song, 0) + 1
	return songsAndQuantity

def extractData(files):
	songDict = numberOfTimesPlayed(files)
	with open("numberOfTimesPlayed.txt", encoding="UTF-8", mode="w") as fout:
		for song in sorted(songDict, key=songDict.get, reverse=True):
		  fout.write(", ".join([str(songDict[song]),str(song)]))
		  fout.write("\n")

if __name__ == "__main__":
	files = getFiles('nml')
	tracklist(files)
	extractData(files)
#	print(files)