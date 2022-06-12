# AutomaticFileOrganizer
A python script to automatically organize all files in a directory to it's own folder and/or any new files in the directory.
Any change in the given directory will trigger the code and attempt to organize the folder again, it does not care if the file is removed or not, 
it will trigger the function that organizes the files regardlessly.

It creates a new folder for each different types of files, for example, for a text file it will create a folder named TEXT in the given directory if a folder named TEXT does not exist already.
It will use the existing folder and not create a new folder if it exists.

WARNING: The script will overwrite any file with the same name and file extension in the folder, which can result in a permanent loss of the previous file.
In the future, I will add a code to rename the file if a file with the same name and extension already exists, till then, be careful.


Here's a short video of it doing its job:
![](https://i.imgur.com/pgUXr65.gif)
