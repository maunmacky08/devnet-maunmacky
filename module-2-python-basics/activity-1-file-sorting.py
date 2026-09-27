"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Macky S. Maun]
Date: [September 27, 2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[I made a program that sorts files into folders based on their file type so for example if file is jpg it will go to images folder then if a txt file it will directly go to documents.]


============================================
KEY VOCABULARY
============================================
- os module: to work with files and folders
- shutil module: used to copy or move files and folders
- file path: location of files or folders
- directory: The folder where files are stored in
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""


import os
import shutil

folder = "files"

for file in os.listdir(folder):
    if file.endswith(".jpg"):
        shutil.move(folder + "/" + file, "Images/" + file)
    elif file.endswith(".txt"):
        shutil.move(folder + "/" + file, "Documents/" + file)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I didn't manage to do this acitivity when it was first introduced to me since I didn't even know what to do yet. But I did it regardless and one mistake I did was making a typo instead of jpg it was jpeg so I definitely wanna avoid doing typo next time]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
