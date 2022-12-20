from rest_framework import serializers

from .models import Setting, TestCategory, Tag, Metadata, Library, Template, TestSuite, TestCase

class TestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCategory
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class TestSuiteSerializer(serializers.ModelSerializer):
    test_category = TestCategorySerializer(many=False)
    tags = TagsSerializer(many=True)
    metadata = MetadataSerializer(many=True)
    libraries = LibrarySerializer(many=True)

    test_cases = serializers.SerializerMethodField()

    def get_test_cases(self, test_suite):
        queryset = TestCase.objects.filter(test_suite_id=test_suite.id)

        return TestCaseSerializer(queryset, many=True).data

    class Meta:
        model = TestSuite
        fields = ('id', 'test_category', 'tags', 'metadata', 'libraries', 'name', 'documentation', 'suite_setup', 'suite_teardown', 'test_setup', 'test_teardown', 'test_timeout', 'source', 'test_cases')

class TestCaseSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    templates = TemplateSerializer(many=True)

    class Meta:
        model = TestCase
        fields = '__all__'

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': False},
            'name': {'validators': []},
        }