# This parser looks for keyword "The patient" and converts it into a unique name

import re
import fileinput
import os, sys
import shutil

# pattern = re.compile("The patient | patient")
# match = re.search(pattern, "The patient gave informed")
# print(match.group(0))

# generate a unique name

# process files and find keyword "The patient"
# compile file in one directory

# create directory for keyword "The patient"
def create_dir(child_dir, parent_dir):
    path1 = parent_dir+"/"+child_dir
    if not os.path.exists(path1):
        #print("directory not exist")
        # use octal number 0755 for python 2 & 0o755 for python 3
        os.mkdir(path1,0o755);
    else:
        print("directory exists")


def find_in_dir(parent_dir):
    new_dir = "male"
    create_dir(new_dir, parent_dir)
    for index in range(2375):
        filename = parent_dir+"/"+str(index)+".txt"
        try:
            f = open(filename,'r')
            filedata = f.read()
            f.close()
        except OSError:
            continue

        m = re.findall('He\s', filedata)
        print(m)
        if m: 
        # if (filedata.find("he") > 0):
            src = parent_dir+"/"+str(index)+".txt"
            dst = parent_dir+"/"+new_dir+"/"+str(index)+".txt"
            shutil.move(src,dst)


target_dir = input("input directory:")
find_in_dir(target_dir)

