from __future__ import print_function
import os
import sys
import shutil
import math
import json
import logging
import shutil


def detect_language(file_path=None):
    """
    Function detects the language of the code.
    Note:
    Yet to be optimised.
    :param file_path:
    :return: name of the language
    """

    file_name = file_path.split('/')[-1]
    language_dict = {"py": "python", "cpp": "cplusplus"}
    if file_name.find('.') == -1:
        print("Please Provide full name of the file with file extn")
    else:
        file_extn = (file_name.split(".")[-1]).lower()
        file_language = language_dict[file_extn]


# yet to complete this function
def add_stdout_stub(file_json):
    """
    Yet to define functioning
    :param file_json:
    :return:
    """
    if file_json["programming_language"] == "python":
        os.system("mv ")



def copy_directory_structure(src, dst, copy_file = False):
    """ Copies the directory or directory structure according
    to the value of copy_file
    """
    if copy_file == True :
        shutil.copytree(src,dst)
    else:
        modified_copytree(src, dst)



def modified_copytree(src, dst):
    """ Modified version of shutil.copytree
    to copy only the directory structure and
    not the files
    """
    if os.path.isdir(src):
        names = os.listdir(src)

        os.makedirs(dst, 0777)
        errors = []
        for name in names:
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                modified_copytree(srcname, dstname)
            except (IOError, os.error) as why:
                errors.append((srcname, dstname, str(why)))
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except Exception as err:
                errors.extend(err.args[0])
        try:
            shutil.copystat(src, dst)
        #except WindowsError:
            # can't copy file access times on Windows
            #pass
        except OSError as why:
            errors.extend((src, dst, str(why)))
        if errors:
            raise Exception(errors)



def changePermission(mode,objectName,File = True):
    if File:
        output = command_run("chmod "+str(mode)+" "+str(objectName))
    else:
        output = command_run("chmod -R "+str(mode)+" "+str(objectName))
    if output[1]:
        pass

def changeOwner(user,group,objectName,File = True):
    if File:
        output = command_run("chown "+str(user)+":"+str(group)+" "+str(objectName))
    else:
        output = command_run("chown -R "+str(user)+":"+str(group)+" "+str(objectName))
    if output[1]:
        pass
