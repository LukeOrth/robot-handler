import ast
from pathlib import Path
from pprint import pprint
from robot.api import get_model
from robot.parsing.model.blocks import TestCase as TestCaseNode
from robot.parsing.model.statements import Documentation, ForceTags, LibraryImport, Metadata, Setup, SuiteSetup, SuiteTeardown, Teardown, Template, TestCaseName, TestSetup, TestTeardown, TestTimeout, Tags, Timeout
from tests.models import FileLocations, TestSuite, TestCase


class TestSuitePrototype:
    def __init__(self):
        self.name = ''
        self.documentation = ''
        self.metadata = []
        self.suite_setup = ''
        self.suite_teardown = ''
        self.force_tags = []
        self.test_setup = ''
        self.test_teardown = ''
        self.test_timeout = ''
        self.libraries = []
        self.path = ''

class TestCasePrototype:
    def __init__(self):
        self.test_suite = None
        self.name = ''
        self.documentation = ''
        self.tags = []
        self.setup = ''
        self.teardown = ''
        self.template = []
        self.timeout = ''
        self.body = ''
        self.path = ''

class RobotParser(ast.NodeVisitor, TestSuitePrototype, TestCasePrototype):

    def __init__(self):
        self.path = None
        self.test_suite = None
        self.test_cases = []

    def visit_File(self, node):
        self.path = node.source
        self.generic_visit(node)

    def visit_SettingSection(self, node):
        ts = TestSuitePrototype()
        # TestSuite: Name
        ts.name = Path(self.path).stem
        # TestSuite: Path
        ts.path = self.path
        for i in ast.iter_child_nodes(node):
            # TestSuite: documentation
            if type(i) == Documentation:
                ts.documentation = i.value
            # TestSuite: metadata
            if type(i) == Metadata:
                ts.metadata.append(f'{i.name}    {i.value}')
            # TestSuite: suite_setup
            if type(i) == SuiteSetup:
                ts.suite_setup = i.name
            # TestSuite: suite_teardown
            if type(i) == SuiteTeardown:
                ts.suite_teardown = i.get_value('NAME')
            # TestSuite: force_tags
            if type(i) == ForceTags:
                for v in i.values:
                    ts.force_tags.append(v)
            # TestSuite: test_setup
            if type(i) == TestSetup:
                ts.test_setup = i.name
            # TestSuite: test_teardown
            if type(i) == TestTeardown:
                ts.test_teardown = i.name
            # TestSuite: test_timeout
            if type(i) == TestTimeout:
                ts.test_timeout = i.value
            # TestSuite: libraries
            if type(i) == LibraryImport:
                ts.libraries.append(i.name)
        self.test_suite = ts

    def visit_TestCaseSection(self, node):
        for test_case in ast.iter_child_nodes(node):
            if type(test_case) == TestCaseNode:
                tc = TestCasePrototype()

                for n in ast.iter_child_nodes(test_case):
                    # TestCase: name
                    if type(n) == TestCaseName:
                        tc.name = n.name
                    # TestCase: documentation
                    if type(n) == Documentation:
                        tc.documentation = n.value
                    # TestCase: tags
                    if type(n) == Tags:
                        for tag in n.values:
                            tc.tags.append(tag)
                    # TestCase: setup
                    if type(n) == Setup:
                        tc.setup = n.name
                    # TestCase: teardown
                    if type(n) == Teardown:
                        tc.teardown = n.name
                    # TestCase: template
                    if type(n) == Template:
                        tc.template = n.value
                    # TestCase: timeout
                    if type(n) == Timeout:
                        tc.timeout = n.value
                    # TestCase: body
                    # WILL REVIST THIS
                self.test_cases.append(tc)

def run(param="Luke was here"):
    # get current robot_dir
    robot_dir = FileLocations.objects.filter(pk='robot_dir').first().location

    if robot_dir:
        test_suites = TestSuite.objects.all()
        test_suites.delete()
        
        p = Path(robot_dir.name)
        for f in p.rglob('*.robot'):
            model = get_model(f)
            parser = RobotParser()
            parser.visit(model)

            ts = TestSuite(**parser.test_suite.__dict__)
            ts.save()

            for test_case in parser.test_cases:
                test_case.test_suite = ts
                tc = TestCase(**test_case.__dict__)
                tc.save()