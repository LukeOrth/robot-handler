from django.http import HttpResponse 
from django.shortcuts import get_object_or_404, redirect, render

from .models import TestSuite, TestCase
from .scripts import testing

def index(request):
    test_suite_list = TestSuite.objects.order_by('name')
    context = {'test_suite_list': test_suite_list}
    return render(request, 'tests/index.html', context)

def refresh_tests(request):
    testing.run('luke was here')
    return redirect('tests:index')

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


