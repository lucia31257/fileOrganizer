import os
import shutil
import datetime
import logging
from enum import Enum


# type of files
# class TFile(Enum):
#     IMAGE = 1
#     DOC = 2
#     MEDIA = 3
#     INSTALLER = 4
#     COMPRESSED = 5
#     EBOOK = 6
#     OTHERS = 7


# sort the files by its extension from file name
def sort_file(filename):
    # get the extension for the give file
    extension = filename.split(".")[-1].lower()
    # file types
    image_ext = ["jpg", "jpeg", "png", "gif", "psd", "heic"]
    doc_ext = ["doc", "docx", "pdf", "tex", "xlsx", "xls", "xlsm"]
    media_ext = ["mp4", "avi", "mkv"]
    installer_ext = ["pkg", "dmg", "exe"]
    compressed_ext = ["zip", "rar", "7z", "tar", "gz", "bz2", "xz"]
    ebook_ext = ["mobi", "epub", "azw4", "txt"]

    if extension in image_ext:
        return "image"
    elif extension in doc_ext:
        return "doc"
    elif extension in media_ext:
        return "media"
    elif extension in installer_ext:
        return "installer"
    elif extension in compressed_ext:
        return "compressed"
    elif extension in ebook_ext:
        return "ebook"
    else:
        return "others"


# find if every folder in the list of folders is the source path, if not create one
# def create_folder(src, folders, files):
#     files_lower = [file.lower for file in files]
#     for f in folders:
#         if f.lower() not in files_lower:
#             os.mkdir(os.path.join(src, f))
#     return


# check if is a file
def is_file(src, file):
    path_f = os.path.join(src, file)
    return os.path.isfile(path_f)


# organize files
def organizer(src):
    files = os.listdir(src)
    for file in files:
        # check if is a regular file
        path_f = os.path.join(src, file)
        if is_file(src, file):
            # check the file type
            f_type = sort_file(file)
            # check if the folder to characterize exist if no create one
            type_folder = os.path.join(src, f_type)
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            # if f_type not in files:
            #     os.mkdir(os.path.join(src, f_type))

            # move the file to the corresponding folder
            destn_path = os.path.join(type_folder, file)
            shutil.move(path_f, destn_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    source = input("Enter the source path:")
    source.replace(" ", "")
    organizer(source)