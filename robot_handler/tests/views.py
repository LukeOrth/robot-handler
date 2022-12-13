from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException


from .forms import RefreshTests, RobotLocation
from .models import FileLocations, TestCategory, TestSuite, TestCase, Tag
from .scripts import update_tests, update_robot_dir
from .serializers import FileLocationsSerializer, TestSuiteSerializer, TestCaseSerializer, TagsSerializer

#ENDPOINT: /api
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'TestSuites': '/v1/test-suites',
    }
    return Response(api_urls)

#ENDPOINT: /api/v1/test-suites
@api_view(['GET'])
def testSuitesList(request):
    test_suites = TestSuite.objects.order_by('test_category__name', 'name')
    serializer = TestSuiteSerializer(test_suites, many=True)
    return Response(serializer.data)

#ENDPOINT: /api/v1/test-suites/<id>
@api_view(['GET'])
def testSuite(request, pk):
    test_suite = TestSuite.objects.get(id=pk)
    serializer = TestSuiteSerializer(test_suite, many=False)
    return Response(serializer.data)

#ENDPOINT: /api/v1/test-cases
@api_view(['GET'])
def testCasesList(request):
    test_cases = TestCase.objects.order_by('name')
    serializer = TestCaseSerializer(test_cases, many=True)
    return Response(serializer.data)

#ENDPOINT: /api/v1/test-cases/<id>
@api_view(['GET'])
def testCase(request, pk):
    test_case = TestCase.objects.get(id=pk)
    serializer = TestCaseSerializer(test_case, many=False)
    return Response(serializer.data)

#ENDPOINT: /api/v1/tags/
@api_view(['GET'])
def tagsList(request):
    tags = Tag.objects.order_by('name')
    serializer = TagsSerializer(tags, many=True)
    return Response(serializer.data)

#ENDPOINT: /api/v1/tests-update/
@api_view(['POST'])
def testsUpdate(request):
    serializer = self.FileLocationsSerializer(data=request.data)
    print(serializer)
    # if serializer.is_valid():
    #     name = serializer.data.name
    #     location = serializer.data.location

    #     if name == 'robot_dir':
    #         robot_dir = FileLocations.objects.filter(pk='robot_dir').first().location.name

    #     if name = 'tests_dir':
    #         tests_dir = FileLocations.objects.filter(pk='tests_dir').first().location.name
        

class ServiceUnavailable(APIException):
    status_code = 404

def index(request):
    test_category_list = TestCategory.objects.order_by('name')
    test_suite_list = TestSuite.objects.order_by('test_category__name', 'name')
    robot_dir = FileLocations.objects.filter(pk='robot_dir').first()

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


