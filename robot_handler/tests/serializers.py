from rest_framework import serializers

from .models import TestSuite, TestCase, Tag

class TestSuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuite
        fields = '__all__'

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    test_suite = TestSuiteSerializer(many=False, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'