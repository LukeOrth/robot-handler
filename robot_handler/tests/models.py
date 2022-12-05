import os
from django.conf import settings
from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Settings(models.Model):
    robot_location = models.FilePathField(path=images_path)

class TestSuite(models.Model):
    name = models.CharField(max_length=200)
    documentation = models.TextField(blank=True)
    metadata = models.CharField(blank=True, max_length=200)
    suite_setup = models.CharField('suite setup', blank=True, max_length=200)
    suite_teardown = models.CharField('suite teardown', blank=True, max_length=200)
    force_tags = models.CharField('force tags', blank=True, max_length=200)
    test_setup = models.CharField('test setup', blank=True, max_length=200)
    test_teardown = models.CharField('test teardown', blank=True, max_length=200)
    test_timeout = models.CharField('test timeout', blank=True, max_length=200)
    library = models.CharField(blank=True, max_length=200)
    path = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name

class TestCase(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=200)
    documentation = models.TextField(blank=True)
    tags = models.CharField(blank=True, max_length=200)
    setup = models.CharField(blank=True, max_length=200)
    teardown = models.CharField(blank=True, max_length=200)
    template = models.CharField(blank=True, max_length=200)
    timeout = models.CharField(blank=True, max_length=200)
    arguments = models.CharField(blank=True, max_length=200)
    body = models.TextField(blank=True)
    path = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name
