from django.contrib import admin

from .models import TestSuite, TestCase

admin.site.register(TestSuite)
admin.site.register(TestCase)

# Register your models here.
