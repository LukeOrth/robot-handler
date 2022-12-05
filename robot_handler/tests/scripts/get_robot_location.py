from django.shortcuts import get_object_or_404
from tkinter import filedialog, Tk
from tests.models import Settings


def run():

    robot_location = Settings(robot_location="/home/luke/projects/robot-handler/robot_handler")
    robot_location.save()

    settings = Settings.objects.first()
    robot_location = getattr(settings, 'robot_location')

    print(robot_location)

    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected