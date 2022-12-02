from tests.models import TestSuite, TestCase

def run(param='nothing entered'):

    test_suites = TestSuite.objects.all()
    test_suites.delete()
    
    ts = TestSuite(name=param)
    ts.save()
