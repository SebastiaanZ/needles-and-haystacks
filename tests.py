import random
import unittest
from string import ascii_uppercase

from functions import haystack_functions


class TestCaseBuilder(unittest.TestCase):
    def __init__(self, methodName='runTest', function=None):
        super().__init__(methodName)
        self.function = function

    @staticmethod
    def create_testcase(testcase, function=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase(name, function=function))
        return suite


class TestHaystackFunctions(TestCaseBuilder):
    def test_short_short_unique_true(self):
        haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        needles = [1, 3, 5, 7, 9]
        self.assertTrue(self.function(haystack, needles))

    def test_short_short_norepeats_false(self):
        haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        needles = [1, 3, 5, 7, 11]
        self.assertFalse(self.function(haystack, needles))

    def test_short_short_repeats_true(self):
        haystack = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        needles = [1, 1, 2, 3, 3, 5]
        self.assertTrue(self.function(haystack, needles))

    def test_short_short_repeats_false(self):
        haystack = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        needles = [1, 1, 2, 3, 3, 6]
        self.assertFalse(self.function(haystack, needles))

    def test_short_short_outoforder(self):
        haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        needles = [1, 3, 5, 4]
        self.assertFalse(self.function(haystack, needles))

    def test_short_short_unique_match(self):
        '''Test if multiple needles are not matched against one item in haystack'''
        haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        needles = [1, 1, 2, 3]
        self.assertFalse(self.function(haystack, needles))

    def test_long_short_unique_true(self):
        random.seed(2019081301)

        for _ in range(5):
            haystack = list(range(1000))
            needles = sorted(random.sample(range(1000), k=5))
            self.assertTrue(self.function(haystack, needles))

    def test_long_short_unique_false(self):
        random.seed(2019081302)

        for _ in range(5):
            haystack = list(range(1000))
            needles = sorted(random.sample(range(1000), k=5)) + [-1]
            self.assertFalse(self.function(haystack, needles))

    def test_long_long_unique_true(self):
        random.seed(2019081303)

        for _ in range(5):
            haystack = list(range(1000))
            needles = sorted(random.sample(range(1000), k=100))
            self.assertTrue(self.function(haystack, needles))

    def test_long_long_unique_false(self):
        random.seed(2019081304)

        for _ in range(5):
            haystack = list(range(1000))
            needles = sorted(random.sample(range(1000), k=100)) + [-1]
            self.assertFalse(self.function(haystack, needles))

    def test_long_long_repeats_true(self):
        random.seed(2019081305)

        for _ in range(5):
            haystack = sorted(list(range(1000))*3)
            needles = sorted(random.sample(range(1000), k=100)*3)
            self.assertTrue(self.function(haystack, needles))

    def test_long_long_repeats_false(self):
        random.seed(2019081306)

        for _ in range(5):
            haystack = sorted(list(range(1000))*3)
            needles = sorted(random.sample(range(1000), k=100)*3 + [500, 500, 500, 500])
            self.assertFalse(self.function(haystack, needles))

    def test_long_long_outoforder(self):
        haystack = list(range(1000))
        needles = list(range(300, 400, 2)) + list(range(500, 480, -2))
        self.assertFalse(self.function(haystack, needles))

    def test_long_long_unique_match(self):
        '''Test if multiple needles are not matched against one item in haystack'''
        haystack = list(range(1000))
        needles = list(range(300, 400)) + [500, 500]
        self.assertFalse(self.function(haystack, needles))

    def test_long_long_identical_lists(self):
        haystack = list(range(10000))
        needles = list(range(10000))
        self.assertTrue(self.function(haystack, needles))

    def test_long_long_small_charset_true(self):
        random.seed(2019081307)

        haystack = random.choices(ascii_uppercase, k=1000)
        needles = haystack[0::len(haystack)//50]
        self.assertTrue(self.function(haystack, needles))


def main(haystack_functionss):
    for name, function in haystack_functionss:
        print(f"Testing haystack function written by {name}")
        print("----------------------------------------------------------------------")
        suite = unittest.TestSuite()
        suite.addTest(TestCaseBuilder.create_testcase(TestHaystackFunctions, function=function))
        unittest.TextTestRunner(verbosity=1).run(suite)
        print("----------------------------------------------------------------------", end="\n\n")


if __name__ == "__main__":
    main(haystack_functions)
