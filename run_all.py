from test_framework.core import TestLoader, TestSuite, TestRunner
from test_framework.tests.test_case_test import TestCaseTest
from test_framework.tests.test_suite_test import TestSuiteTest
from test_framework.tests.test_loader_test import TestLoaderTest


loader = TestLoader()
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_load_suite = loader.make_suite(TestLoaderTest)

suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_load_suite)

runner = TestRunner()
runner.run(suite)