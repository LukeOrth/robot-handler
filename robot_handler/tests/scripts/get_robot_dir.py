from django.shortcuts import get_object_or_404
from tkinter import filedialog, Tk
from tests.models import FileLocations


def run():

    root = Tk()
    root.withdraw()
    dir_selected = filedialog.askdirectory()
    print(dir_selected)

    FileLocations.objects.filter(pk='robot_dir').update(location=dir_selected)