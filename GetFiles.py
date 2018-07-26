from os import listdir
from Constants import FILE_RE

import re

def getFiles(extension):
	files = listdir("history/")
	filesWithExtension = list(filter(lambda x: re.search(FILE_RE, x), files))

	return filesWithExtension