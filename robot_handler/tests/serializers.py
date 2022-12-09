from rest_framework import serializers

from .models import TestSuite, TestCase

class TestSuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuite
        fields = (
            "id",
            "name",
            "test_category",
            "documentation",
            "suite_setup",
            "test_teardown",
            "test_timeout",
            "source"
        )