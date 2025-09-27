#   To import 'ZipFile class' from 'zipfile module'
from zipfile import ZipFile

#   To create zip file by adding 2 files
with ZipFile("zipper.zip", "w") as zf:
    zf.write("file1.txt")
    zf.write("file2.txt")

#   To extract files from zip file to a folder
with ZipFile("zipper.zip") as zf:
    zf.extractall("extract_folder/")

# To see the effects of the entire code above, delete created zip file & the folder used for extracting files before rerunning