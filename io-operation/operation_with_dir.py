import os
from datetime import datetime

dirlist = os.scandir("test_dir/") # scan the dir
for mdir in dirlist: # list of the dir and iterate through them.
    print(mdir.is_dir()) # check dir or not
    print(mdir.is_file()) # check file or not


# checking when the dir created
dirlist = os.scandir("test_dir/")
for mdir in dirlist:
    print(mdir.stat().st_mtime)

# function for converting .stat().st_mtime time in a regular format
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date
# here is convert_data function used
dirlist = os.scandir("test_dir/")
for mdir in dirlist:
    print(mdir.name,"Last Modified: ",convert_date(mdir.stat().st_mtime))

# get all the file or dir from the dir
dirlist = os.listdir("test_dir/")
for mdir in dirlist:
    print(mdir)


#  getting all file which has .log file extension
import os
import fnmatch
for file_name in os.listdir('test_dir/'):
    if fnmatch.fnmatch(file_name, '*.log'):
        print(file_name)