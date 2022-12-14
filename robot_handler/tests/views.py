from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from pathlib import Path
import json

from .forms import RefreshTests, RobotLocation
from .models import Setting, TestCategory, TestSuite, TestCase, Tag
from .scripts import update_tests, update_robot_dir
from .serializers import SettingSerializer, TestSuiteSerializer, TestCaseSerializer, TagsSerializer

#ENDPOINT: /api
class ApiOverview(APIView):
    # ENDPOINTS:
    #   /api/
    
    def get(self, request, format=None):
        api_urls = {
            'Test Suites': '/v1/test-suites',
            'Test Suite': '/v1/test-suites/<id>',
            'Test Cases': '/v1/test-cases',
            'Test Case': '/v1/test-cases/<id>',
            'Tags': '/v1/tags/',
            'Tag': '/v1/tag/<name>',
            'Settings': '/v1/settings/',
            'Setting': '/v1/settings/?name=<name>',
            'Update Tests': '/v1/update-tests/'
        }

        return Response(api_urls)

class TestSuites(APIView):
    # ENDPOINTS: 
    #   /api/v1/test-suites/
    #   /api/v1/test-suites/<id>

    def get_queryset(self):
        test_suites = TestSuite.objects.order_by('test_category__name', 'name')

        return test_suites
    
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs["id"]
            if id:
                test_suite = TestSuite.objects.get(id=id)
                serializer = TestSuiteSerializer(test_suite)
        except:
            test_suites = self.get_queryset()
            serializer = TestSuiteSerializer(test_suites, many=True)
        
        return Response(serializer.data)

class TestCases(APIView):
    # ENDPOINTS:
    #   /api/v1/test-cases/
    #   /api/v1/test-cases/<id>

    def get_queryset(self):
        test_cases = TestCase.objects.order_by('name')

        return test_cases
    
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs["id"]
            if id:
                test_case = TestCase.objects.get(id=id)
                serializer = TestCaseSerializer(test_case)
        except:
            test_cases = self.get_queryset()
            serializer = TestCaseSerializer(test_cases, many=True)

        return Response(serializer.data)

class Tags(APIView):
    # ENDPOINTS:
    #   /api/v1/tags/
    #   /api/v1/tags/<id>

    def get_queryset(self):
        tags = Tag.objects.order_by('name')

        return tags

    def get(self, request, *args, **kwargs):
        try:
            name = kwargs["name"]
            if name:
                tag = Tag.objects.get(name=name)
                serializer = TagsSerializer(tag)
        except:
            tags = self.get_queryset()
            serializer = TagsSerializer(tags, many=True)

        return Response(serializer.data)

class Settings(APIView):
    # ENDPOINTS:
    #   /api/v1/settings/
    #   /api/v1/settings/?name=<name>

    def get_queryset(self):
        setting_values = Setting.objects.order_by('name')

        return setting_values

    def get(self, request, *args, **kwargs):
        try:
            name = request.query_params["name"]
            if name:
                setting_value = Setting.objects.get(name=name)
                serializer = SettingSerializer(setting_value)
        except:
            setting_values = self.get_queryset()
            print(setting_values)
            serializer = SettingSerializer(setting_values, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SettingSerializer(data=request.data)
        if serializer.is_valid():
            try:
                setting = Setting.objects.get(name=serializer.data['name'])
                setting.value = serializer.data['value']
                setting.save()

                return Response(SettingSerializer(setting).data, status=status.HTTP_201_CREATED)
            except:
                response = {'name': ["Couldn't find a setting with this name."]}

                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTests(APIView):
    # ENDPOINTS:
    #   /api/v1/update-tests/

    def post(self, request, format=None):
        tests_dir = Setting.objects.filter(pk='tests_dir').first().value
        if tests_dir:
            update_tests.run(tests_dir)
            
            return Response(request.data)
        else:
            error = {'error': "No 'tests_dir' found in settings.  Unable to update tests."}

            return Response(data=error, status=status.HTTP_400_BAD_REQUEST)

class ServiceUnavailable(APIException):
    status_code = 404

def index(request):
    test_category_list = TestCategory.objects.order_by('name')
    test_suite_list = TestSuite.objects.order_by('test_category__name', 'name')
    robot_dir = Setting.objects.filter(pk='robot_dir').first()

    context = {
        'test_category_list': test_category_list,
        'robot_dir': robot_dir,
        'test_suite_list': test_suite_list,
    }
    return render(request, 'tests/index.html', context)

def vue_test(request):
    return render(request, 'tests/vue_test.html')

def refresh_tests(request):
    refresh_tests_form = None
    robot_location_form = None
    if request.method == 'POST':
        if 'refresh_tests' in request.POST:
            refresh_tests_form = RefreshTests(request.POST)
            update_tests.run()
            return redirect(request.META.get('HTTP_REFERER'))
        if 'robot_location' in request.POST:
            robot_location_form = RobotLocation(request.POST)
            update_robot_dir.run()
            return redirect(request.META.get('HTTP_REFERER'))
    context = {
        'refresh_tests_form': refresh_tests_form,
        'robot_location_form': robot_location_form,
    }
    return render(request, request.META.get('HTTP_REFERER'), context=context)

def test_suite(request, test_suite_id):
    test_suite = get_object_or_404(TestSuite, pk=test_suite_id)
    return render(request, 'tests/test_suite.html', {'test_suite': test_suite})

def test_suite_results(request, test_suite_id):
    response = "You're looking at the results of test suite %s."
    return HttpResponse(response % test_suite_id)

def test_suite_run(request, test_suite_id):
    return HttpResponse("You're running test suite %s." % test_suite_id)

def test_case(request, test_suite_id, test_case_id):
    test_case = get_object_or_404(TestCase, pk=test_case_id)
    return render(request, 'tests/test_case.html', {'test_case': test_case})

def test_case_results(request, test_case_id):
    response = "You're looking at the results of test case %s."
    return HttpResponse(response % test_case_id)

def test_case_run(request, test_case_id):
    return HttpResponse("You're running test case %s." % test_case_id)


