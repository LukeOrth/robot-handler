from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import TestSuite, TestCase

def index(request):
    test_suite_list = TestSuite.objects.order_by('name')
    context = {'test_suite_list': test_suite_list}
    return render(request, 'tests/index.html', context)

def test_suite(request, test_suite_id):
    test_suite = get_object_or_404(TestSuite, pk=test_suite_id)
    return render(request, 'tests/test_suite.html', {'test_suite': test_suite})

def test_case(request, test_case_id):
    test_case = get_object_or_404(TestCase, pk=test_case_id)
    return render(request, 'tests/test_case.html', {'test_case': test_case})

def results(request, test_suite_id):
    response = "You're looking at the results of test suite %s."
    return HttpResponse(response % test_suite_id)

def run(request, test_suite_id):
    return HttpResponse("You're running test suite %s." % test_suite_id)
