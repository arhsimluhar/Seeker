from __future__ import print_function
import os
import sys
import math
import json
import logging


def detect_language(file_path=None):
    file_name = file_path.split('/')[-1]
    language_dict = {"py": "python", "cpp": "cplusplus"}
    if file_name.find('.') == -1:
        print("Please Provide full name of the file with file extn")
    else:
        file_extn = (file_name.split(".")[-1]).lower()
        file_language = language_dict[file_extn]





def add_stdout_stub(file_json):
    if file_json["programming_language"] == "python":
        os.system("mv ")
