import os
from django.shortcuts import get_object_or_404
from pathlib import Path
from tkinter import filedialog, Tk
from tests.models import Setting


# Function for finding the "/tests" directory in robot project
def get_tests_dir(rootdir):

    for folder, subfolders, files in os.walk(rootdir):
        for s in subfolders:
            if s.endswith("tests"):
                return os.path.join(folder, s)

    return None
 
def run():

    # Use Tkinter to get the robot project directory from user
    root = Tk()
    root.withdraw()
    dir_selected = filedialog.askdirectory()

    if dir_selected:
        tests_dir = get_tests_dir(dir_selected)
        if tests_dir:
            # Update robot_dir in DB
            Setting.objects.filter(pk='robot_dir').update(value=dir_selected)
            # Get the robot_dir from DB
            robot_dir = Setting.objects.filter(pk='robot_dir').first().value
            # Update tests_dir in DB
            Setting.objects.filter(pk='tests_dir').update(value=tests_dir)