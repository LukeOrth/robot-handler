from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import TestSuite, TestCase

def index(request):
    test_suite_list = TestSuite.objects.order_by('name')
    context = {'test_suite_list': test_suite_list}
    return render(request, 'tests/index.html', context)

def detail(request, test_suite_id):
    test_suite = get_object_or_404(TestSuite, pk=test_suite_id)
    return render(request, 'tests/detail.html', {'test_suite': test_suite})

def results(request, test_suite_id):
    response = "You're looking at the results of test suite %s."
    return HttpResponse(response % test_suite_id)

def run(request, test_suite_id):
    return HttpResponse("You're running test suite %s." % test_suite_id)
