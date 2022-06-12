import os
import shutil
from time import sleep

def organizefiles():
	for file in checkdircontent(filedir):
		try:
			if file.lower().endswith(fileextensionsF["video"]):
				if os.path.isdir(filedir + "\\VIDEO"):
					shutil.move(os.path.join(filedir,file), os.path.join(filedir + "\\VIDEO", file))
				else:
					os.mkdir(filedir + "\\VIDEO")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\VIDEO", file))
		except FileNotFoundError:
			pass

		try:
			if file.lower().endswith(fileextensionsF["image"]):
				if os.path.isdir(filedir + "\\IMAGE"):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\IMAGE", file))
				else:
					os.mkdir(filedir + "\\IMAGE")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\IMAGE", file))
		except FileNotFoundError:
			pass

		try:
			if file.lower().endswith(".gif"):
				if os.path.isdir(filedir + "\\GIF"):
					shutil.move(os.path.join(filedir,file), os.path.join(filedir + "\\GIF", file))
				else:
					os.mkdir(filedir + "\\GIF")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\GIF", file))
		except FileNotFoundError:
			pass

		try:
			if file.lower().endswith(".txt"):
				if os.path.isdir(filedir + "\\TEXT"):
					shutil.move(os.path.join(filedir,file), os.path.join(filedir + "\\TEXT", file))
				else:
					os.mkdir(filedir + "\\TEXT")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\TEXT", file))
		except FileNotFoundError:
			pass

		try:
			if file.lower().endswith(fileextensionsF["audio"]):
				if os.path.isdir(filedir + "\\AUDIO"):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\AUDIO", file))
				else:
					os.mkdir(filedir + "\\AUDIO")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\AUDIO", file))
		except FileNotFoundError:
			pass

		try:
			if file.lower().endswith(fileextensionsF["archive"]):
				if os.path.isdir(filedir + "\\ARCHIVE"):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\ARCHIVE", file))
				else:
					os.mkdir(filedir + "\\ARCHIVE")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\ARCHIVE", file))
		except FileNotFoundError:
			pass

		try:
			if file.lower().endswith(".exe"):
				if os.path.isdir(filedir + "\\EXECUTABLE"):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\EXECUTABLE", file))
				else:
					os.mkdir(filedir + "\\EXECUTABLE")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + "\\EXECUTABLE", file))
		except FileNotFoundError:
			pass



# Automatic File Organizer #
# Organizes the files in the Desktop folder at start-up and when a file is added, modified or removed #
# Made by Asux - 12/06/2022 #




fileextensionsF = {
	"video":(".webm",".mpg",".mp2",".mpeg",".mpe",".mpv",".ogg",".mp4",".m4p",
	         ".m4v",".avi",".wmv",".wmv",".mov",".qt",".flv",".swf"),
	"image":(".png",".jpg",".jpeg",".webp",".bmp",".raw",".jpe",".jif",".jfif",
	         ".jfi",".dib",".heif",".ind",".jpm",".jp2"),
	"audio":(".m4a",".mp3",".wav",".flac",".wma",".aac",".3gp"),
	"archive":(".zip",".rar",".tar",".7z",".iso",".gz")
}

def checkdircontent(dirpath):
	return os.listdir(dirpath)

filedir = "YOUR PATH HERE"
DC = list()

while True:
	sleep(3)
	if DC == checkdircontent(filedir):
		pass
	else:
		organizefiles()
		DC = checkdircontent(filedir)
