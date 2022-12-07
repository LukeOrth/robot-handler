import ast
from pathlib import Path
from pprint import pprint
from robot.api import get_model
from robot.parsing.model.blocks import TestCase as TestCaseNode
from robot.parsing.model.statements import Documentation, ForceTags, LibraryImport, Metadata as MetadataNode, Setup, SuiteSetup, SuiteTeardown, Teardown, Template, TestCaseName, TestSetup, TestTeardown, TestTimeout, Tags as TagsNode, Timeout
from tests.models import FileLocations, TestSuite, TestCase, Tags, Metadata, Libraries, Templates


class TestSuitePrototype:
    def __init__(self):
        self.name = ''
        self.documentation = ''
        self.suite_setup = ''
        self.suite_teardown = ''
        self.test_setup = ''
        self.test_teardown = ''
        self.test_timeout = ''
        self.path = ''

class TestCasePrototype:
    def __init__(self):
        self.test_suite = None
        self.name = ''
        self.documentation = ''
        self.setup = ''
        self.teardown = ''
        self.timeout = ''
        self.body = ''
        self.path = ''

class TagsPrototype:
    def __init__(self):
        self.test_suite = None
        self.test_case = None
        self.name = None

class MetadataPrototype:
    def __init__(self):
        self.test_suite = None
        self.name = None
        self.value = None

class LibrariesPrototype:
    def __init__(self):
        self.test_suite = None
        self.name = None

class TemplatesPrototype:
    def __init__(self):
        self.test_case = None
        self.name = None

class RobotParser(ast.NodeVisitor, TestSuitePrototype, TestCasePrototype, TagsPrototype):

    def __init__(self):
        self.path = None
        self.test_suite = None
        self.test_cases = []
        self.tags = []
        self.metadata = []
        self.libraries = []
        self.templates = []

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
            # Metadata
            if type(i) == MetadataNode:
                md = MetadataPrototype()
                md.name = i.name
                md.value = i.value
                self.metadata.append(md)
            # TestSuite: suite_setup
            if type(i) == SuiteSetup:
                ts.suite_setup = i.name
            # TestSuite: suite_teardown
            if type(i) == SuiteTeardown:
                ts.suite_teardown = i.get_value('NAME')
            # Tags
            if type(i) == ForceTags:
                for tag in i.values:
                    ts_tags = TagsPrototype()
                    ts_tags.test_suite = True
                    ts_tags.name = tag
                    self.tags.append(ts_tags)
            # TestSuite: test_setup
            if type(i) == TestSetup:
                ts.test_setup = i.name
            # TestSuite: test_teardown
            if type(i) == TestTeardown:
                ts.test_teardown = i.name
            # TestSuite: test_timeout
            if type(i) == TestTimeout:
                ts.test_timeout = i.value
            # Libraries
            if type(i) == LibraryImport:
                lib = LibrariesPrototype()
                lib.name = i.name
                self.libraries.append(lib)
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
                    # Tags
                    if type(n) == TagsNode:
                        for tag in n.values:
                            tc_tags = TagsPrototype()
                            tc_tags.test_case = True
                            tc_tags.name = tag
                            self.tags.append(tc_tags)
                    # TestCase: setup
                    if type(n) == Setup:
                        tc.setup = n.name
                    # TestCase: teardown
                    if type(n) == Teardown:
                        tc.teardown = n.name
                    # Templates
                    if type(n) == Template:
                        tmp = TemplatesPrototype()
                        tmp.name = n.value
                        self.templates.append(tmp)
                    # TestCase: timeout
                    if type(n) == Timeout:
                        tc.timeout = n.value
                    # TestCase: body
                        # PUT BODY HERE
                        # WILL REVIST THIS
                self.test_cases.append(tc)

def update_tags(tags, fk):
    if type(fk) == TestCase:
        for t in tags:
            if t.test_case:
                t.test_case = fk
    if type(fk) == TestSuite:
        for t in tags:
            if t.test_suite:
                t.test_suite = fk


        
def run(param="Luke was here"):

    # get current robot_dir
    robot_dir = FileLocations.objects.filter(pk='robot_dir').first().location

    if robot_dir:
        test_cases = TestCase.objects.all().delete()
        test_suites = TestSuite.objects.all().delete()
        tags = Tags.objects.all().delete()
        
        p = Path(robot_dir.name)
        for f in p.rglob('*.robot'):
            model = get_model(f)
            parser = RobotParser()
            parser.visit(model)

            ts = TestSuite(**parser.test_suite.__dict__)
            ts.save()

            update_tags(parser.tags, ts)

            for meta_data in parser.metadata:
                meta_data.test_suite = ts
                md = Metadata(**meta_data.__dict__)
                md.save()

            for library in parser.libraries:
                library.test_suite = ts
                lib = Libraries(**library.__dict__)
                lib.save()

            for test_case in parser.test_cases:
                test_case.test_suite = ts
                tc = TestCase(**test_case.__dict__)
                tc.save()

                update_tags(parser.tags, tc)

                for template in parser.templates:
                    template.test_case = tc
                    tmp = Templates(**template.__dict__)
                    tmp.save()

            for tag in parser.tags:
                t = Tags(**tag.__dict__)
                t.save()