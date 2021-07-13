from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtest import SearchTest

assertionsTest = TestLoader().loadTestsFromTestCase(AssertionsTest)
searchTest = TestLoader().loadTestsFromTestCase(SearchTest)

smokeTest = TestSuite([assertionsTest, searchTest])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smokeTest)