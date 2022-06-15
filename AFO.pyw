# AFO #
# v0.3 #

# Directory path
path = "C:\\Users\\Asux\\Desktop" # Enter your desired path in this variable
# Additional options
runonce = False # Make it True if you only want to run this script once


# DO NOT EDIT ANYTHING BELOW IF YOU DO NOT KNOW WHAT YOU ARE DOING #

import os
import shutil
from time import sleep

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

fdnames = ("\\VIDEO","\\IMAGE","\\GIF","\\TEXT","\\AUDIO","\\ARCHIVE","\\EXECUTABLE","\\DOCUMENT")

def chkdircont(path):
    return os.listdir(path)
    
def organizefiles():
    for file in chkdircont(path):
        renfile = None
        for name in fdnames:
            if os.path.isfile(path + name + "\\" + file):
                print("A file with the same name as the target file's already exists, attempting to rename the target file")
                newf = file.split(".")
                count = 2
                while os.path.isfile(path + name + "\\" + newf[0] + " (" + str(count) + ")" + "." + newf[1]):
                    count += 1
                renfile = os.rename(path + name + "\\" + file, path + name + "\\" + newf[0] + " (" + str(count) + ")" + "." + newf[1])
                print("Renamed the target file\n")
            else:
                renfile = file
                print("No file with the sane name as the target file's exists, continuing without renaming the target file\n")
        try:
            if renfile.lower().endswith(fileextensionsF["video"]):
                if os.path.isdir(path + fdnames[0]):
                    shutil.move(os.path.join(path,renfile), os.path.join(path + fdnames[0], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[0] + "\n")
                else:
                    os.mkdir(path + fdnames[0])
                    print(path + fdnames[0] + " did not exist, created one")
                    shutil.move(os.path.join(path, file), os.path.join(path + fdnames[0], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[0] + "\n")
            if renfile.lower().endswith(fileextensionsF["image"]):
                if os.path.isdir(path + fdnames[1]):
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[1], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[1] + "\n")
                else:
                    os.mkdir(path + fdnames[1])
                    print(path + fdnames[1] + " did not exist, created one")
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[1], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[1] + "\n")
            if renfile.lower().endswith(".gif"):
                if os.path.isdir(path + fdnames[2]):
                    shutil.move(os.path.join(path,renfile), os.path.join(path + fdnames[2], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[2] + "\n")
                else:
                    os.mkdir(path + fdnames[2])
                    print(path + fdnames[2] + " did not exist, created one")
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[2], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[2] + "\n")
            if renfile.lower().endswith(".txt"):
                if os.path.isdir(path + fdnames[3]):
                    shutil.move(os.path.join(path,renfile), os.path.join(path + fdnames[3], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[3] + "\n")
                else:
                    os.mkdir(path + fdnames[3])
                    print(path + fdnames[3] + " did not exist, created one")
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[3], renfile))
                    print("Moved " + file + " to " + path + fdnames[3] + "\n")
            if renfile.lower().endswith(fileextensionsF["audio"]):
                if os.path.isdir(path + fdnames[4]):
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[4], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[4] + "\n")
                else:
                    os.mkdir(path + fdnames[4])
                    print(path + fdnames[4] + " did not exist, created one")
                    shutil.move(os.path.join(path, file), os.path.join(path + fdnames[4], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[4] + "\n")
            if renfile.lower().endswith(fileextensionsF["archive"]):
                if os.path.isdir(path + fdnames[5]):
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[5], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[5] + "\n")
                else:
                    os.mkdir(path + fdnames[5])
                    print(path + fdnames[5] + " did not exist, created one")
                    shutil.move(os.path.join(path, file), os.path.join(path + fdnames[5], file))
                    print("Moved " + file + " to " + path + fdnames[5] + "\n")
            if renfile.lower().endswith(".exe"):
                if os.path.isdir(path + fdnames[6]):
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[6], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[6] + "\n")
                else:
                    os.mkdir(path + fdnames[6])
                    print(path + fdnames[6] + " did not exist, created one")
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[6], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[6] + "\n")
            if renfile.lower().endswith(fileextensionsF["doc"]):
                if os.path.isdir(path + fdnames[7]):
                    shutil.move(os.path.join(path, file), os.path.join(path + fdnames[7], renfile))
                    print("Moved " + file + " to " + path + fdnames[7] + "\n")
                else:
                    os.mkdir(path + fdnames[7])
                    print(path + fdnames[7] + " did not exist, created one")
                    shutil.move(os.path.join(path, renfile), os.path.join(path + fdnames[7], renfile))
                    print("Moved " + renfile + " to " + path + fdnames[7] + "\n")
        except FileNotFoundError as err:
            print("FileNotFoundError occurred: " + err)
            quit()

while not runonce:
    sleep(3)
    if DC == chkdircont(path):
        print("No changes detected\n")
    elif DC != chkdircont(path):
        print("Changes detected\n")
        organizefiles()
        DC = chkdircont(path)

if runonce:
    organizefiles()
else:
    pass
