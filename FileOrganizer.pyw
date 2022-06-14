# Directory path
filedir = "YOUR_PATH_HERE" # Enter your desired path in this variable
# Additional options
continuechecking = True # Make it False if you only want to run this script once
debug = False # Make it True if you want to debug the program, rename the file extension from .pyw to .py to see the outputs


# DO NOT EDIT ANYTHING BELOW IF YOU DO NOT KNOW WHAT YOU ARE DOING #

import os
import shutil
from time import sleep
import threading

threads = []
def main():
  for item in list:
     t = threading.Thread(target=dgprt, args=(item,))
     threads.append(t)
     t.start()
  for t in threads:
     t.join()

DC = list()
fileextensionsF = {
	"video":(".webm",".mpg",".mp2",".mpeg",".mpe",".mpv",".ogg",".mp4",".m4p",
	         ".m4v",".avi",".wmv",".wmv",".mov",".qt",".flv",".swf"),
	"image":(".png",".jpg",".jpeg",".webp",".bmp",".raw",".jpe",".jif",".jfif",
	         ".jfi",".dib",".heif",".ind",".jpm",".jp2"),
	"audio":(".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".vox", ".wav", ".wma", ".flac"),
	"archive":(".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"),
	"doc":(".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
            ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
            ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
            "pptx", ".pdf")
}

def chkdircont(path):
	return os.listdir(path)

def dgprt(text):
	if debug == True:
		print(text)
	else:
		pass

def organizefiles():
	fdnames = "\\VIDEO","\\IMAGE","\\GIF","\\TEXT","\\AUDIO","\\ARCHIVE","\\EXECUTABLE","\\DOCUMENT"
	for file in chkdircont(filedir):
		try:
			if file.lower().endswith(fileextensionsF["video"]):
				if os.path.isdir(filedir + fdnames[0]):
					shutil.move(os.path.join(filedir,file), os.path.join(filedir + fdnames[0], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[0] + "\n")
				else:
					os.mkdir(filedir + fdnames[0])
					dgprt(filedir + fdnames[0] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[0], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[0] + "\n")
			if file.lower().endswith(fileextensionsF["image"]):
				if os.path.isdir(filedir + fdnames[1]):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[1], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[1] + "\n")
				else:
					os.mkdir(filedir + fdnames[1])
					dgprt(filedir + fdnames[1] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[1], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[1] + "\n")
			if file.lower().endswith(".gif"):
				if os.path.isdir(filedir + fdnames[2]):
					shutil.move(os.path.join(filedir,file), os.path.join(filedir + fdnames[2], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[2] + "\n")
				else:
					os.mkdir(filedir + fdnames[2])
					dgprt(filedir + fdnames[2] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[2], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[2] + "\n")
			if file.lower().endswith(".txt"):
				if os.path.isdir(filedir + fdnames[3]):
					shutil.move(os.path.join(filedir,file), os.path.join(filedir + fdnames[3], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[3] + "\n")
				else:
					os.mkdir(filedir + fdnames[3])
					dgprt(filedir + fdnames[3] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[3], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[3] + "\n")
			if file.lower().endswith(fileextensionsF["audio"]):
				if os.path.isdir(filedir + fdnames[4]):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[4], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[4] + "\n")
				else:
					os.mkdir(filedir + fdnames[4])
					dgprt(filedir + fdnames[4] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[4], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[4] + "\n")
			if file.lower().endswith(fileextensionsF["archive"]):
				if os.path.isdir(filedir + fdnames[5]):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[5], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[5] + "\n")
				else:
					os.mkdir(filedir + fdnames[5])
					dgprt(filedir + fdnames[5] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[5], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[5] + "\n")
			if file.lower().endswith(".exe"):
				if os.path.isdir(filedir + fdnames[6]):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[6], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[6] + "\n")
				else:
					os.mkdir(filedir + fdnames[6])
					dgprt(filedir + fdnames[6] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[6], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[6] + "\n")
			if file.lower().endswith(fileextensionsF["doc"]):
				if os.path.isdir(filedir + fdnames[7]):
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[7], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[7] + "\n")
				else:
					os.mkdir(filedir + fdnames[7])
					dgprt(filedir + fdnames[7] + " did not exist, created one")
					shutil.move(os.path.join(filedir, file), os.path.join(filedir + fdnames[7], file))
					dgprt("Moved " + file + " to " + filedir + fdnames[7] + "\n")
		except:
			pass


while continuechecking:
	sleep(3)
	if DC == chkdircont(filedir):
		dgprt("No changes detected\n")
	else:
		dgprt("Changes detected\n")
		organizefiles()
		DC = chkdircont(filedir)
