import ast, os
from pathlib import Path
from pprint import pprint
from robot.api import get_model
from robot.parsing.model.blocks import TestCase as TestCaseNode
from robot.parsing.model.statements import Documentation, ForceTags, LibraryImport, Metadata as MetadataNode, Setup, SuiteSetup, SuiteTeardown, Teardown, Template as TemplateNode, TestCaseName, TestSetup, TestTeardown, TestTimeout, Tags as TagsNode, Timeout
from tests.models import FileLocations, TestCategory, TestSuite, TestCase, Tag, Metadata, Library, Template

class TestCategoryPrototype:
    def __init__(self):
        self.name = None

class TestSuitePrototype:
    def __init__(self):
        self.name = ''
        self.test_category = None
        self.documentation = ''
        self.suite_setup = ''
        self.suite_teardown = ''
        self.test_setup = ''
        self.test_teardown = ''
        self.test_timeout = ''
        self.source = ''

class TestCasePrototype:
    def __init__(self):
        self.test_suite = None
        self.name = ''
        self.documentation = ''
        self.setup = ''
        self.teardown = ''
        self.timeout = ''
        self.body = ''
        self.source = ''

class TagPrototype:
    def __init__(self):
        self.name = None

class MetadataPrototype:
    def __init__(self):
        self.name = None
        self.value = None

class LibraryPrototype:
    def __init__(self):
        self.name = None

class TemplatePrototype:
    def __init__(self):
        self.name = None

class RobotParser(ast.NodeVisitor):

    def __init__(self):
        self.source = None
        self.category = None
        self.test_suite = None
        self.test_cases = []
        self.test_suite_tags = []
        self.test_case_tags = []
        self.metadata = []
        self.libraries = []
        self.templates = []

    def visit_File(self, node):
        self.source = node.source
        self.generic_visit(node)

    def visit_SettingSection(self, node):
        ts = TestSuitePrototype()

        # TestSuite: Name
        ts.name = Path(self.source).stem
        # TestSuite: Path
        ts.source = self.source

        cat = TestCategoryPrototype()

        # TestCategory
        path = os.path.dirname(ts.source)
        cat.name = os.path.basename(path)
        self.category = cat

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
            # TestSuite: tag
            if type(i) == ForceTags:
                for tag in i.values:
                    ts_tags = TagPrototype()
                    ts_tags.name = tag
                    self.test_suite_tags.append(ts_tags)
            # TestSuite: test_setup
            if type(i) == TestSetup:
                ts.test_setup = i.name
            # TestSuite: test_teardown
            if type(i) == TestTeardown:
                ts.test_teardown = i.name
            # TestSuite: test_timeout
            if type(i) == TestTimeout:
                ts.test_timeout = i.value
            # Library
            if type(i) == LibraryImport:
                lib = LibraryPrototype()
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
                    # Tag
                    if type(n) == TagsNode:
                        for tag in n.values:
                            tc_tags = TagPrototype()
                            tc_tags.name = tag
                            self.test_case_tags.append(tc_tags)
                    # TestCase: setup
                    if type(n) == Setup:
                        tc.setup = n.name
                    # TestCase: teardown
                    if type(n) == Teardown:
                        tc.teardown = n.name
                    # Template
                    if type(n) == TemplateNode:
                        tmp = TemplatePrototype()
                        tmp.name = n.value
                        self.templates.append(tmp)
                    # TestCase: timeout
                    if type(n) == Timeout:
                        tc.timeout = n.value
                    # TestCase: body
                        # PUT BODY HERE
                        # WILL REVIST THIS
                self.test_cases.append(tc)


def run():

    # Get the "/tests" directory from DB
    tests_dir = FileLocations.objects.filter(pk='tests_dir').first().location

    if tests_dir:
        TestCategory.objects.all().delete()
        TestCase.objects.all().delete()
        TestSuite.objects.all().delete()
        Tag.objects.all().delete()
        Metadata.objects.all().delete()
        Library.objects.all().delete()
        Template.objects.all().delete()
        
        p = Path(tests_dir.name)
        for f in p.rglob('*.robot'):
            model = get_model(f)
            parser = RobotParser()
            parser.visit(model)

            cat = TestCategory(**parser.category.__dict__)
            cat.save()

            parser.test_suite.test_category = cat

            ts = TestSuite(**parser.test_suite.__dict__)
            ts.save()

            for tag in parser.test_suite_tags:
                t = Tag(**tag.__dict__)
                t.save()
                ts.tags.add(t)

            for metadata in parser.metadata:
                md = Metadata(**metadata.__dict__)
                md.save()
                ts.metadata.add(md)

            for library in parser.libraries:
                lib = Library(**library.__dict__)
                lib.save()
                ts.libraries.add(lib)

            for test_case in parser.test_cases:
                test_case.test_suite = ts
                tc = TestCase(**test_case.__dict__)
                tc.save()

                for tag in parser.test_case_tags:
                    t = Tag(**tag.__dict__)
                    t.save()
                    tc.tags.add(t)

                for template in parser.templates:
                    tmp = Template(**template.__dict__)
                    tmp.save()
                    tc.templates.add(tmp)