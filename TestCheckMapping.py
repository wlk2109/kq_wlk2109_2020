import unittest
import time
from CheckMapping import CheckMapping

checker = CheckMapping()
check = checker.check_mapping
check1 = checker.check_mapping_better

class TestCheckMapping(unittest.TestCase):

    def test_single_char(self):
        testname= "Single"
        t0 = time.time()

        self.assertTrue()

        elapsed = (time.time()-t0)
        print(f"Test: {testname} took {elapsed} seconds.")

    def test_short_true(self):
        testname= "Short True"
        t0 = time.time()

        self.assertTrue(check('abc', 'def'))

        elapsed = (time.time()-t0)
        print(f"Test: {testname} took {elapsed} seconds.")

    def test_short_false(self):
        testname = "Short False"
        t0 = time.time()

        self.assertFalse(check('abc', 'bbb'))

        elapsed = (time.time() - t0)
        print(f"Test: {testname} took {elapsed} seconds.")

    def test_long_true(self):
        testname = "Long True"
        t0 = time.time()
        s1 = 'aaaabbbccdeffggghhhhiiiijjjkklmnnoopppqqqqrrrrsssttuvwwxxxyyyyzzzz'
        s2 = 'aaaabbbccdeffggghhhhiiiijjjkklmnnoopppqqqqrrrrsssttuvwwxxxyyyyzzzz'

        self.assertTrue(check(s1, s1))

        elapsed = (time.time() - t0)
        print(f"Test: {testname} took {elapsed} seconds.")


    def test_long_single_true(self):
        testname = "Medium Single True"
        t0 = time.time()
        s1 = 'abcdefghijklmnop'
        s2 = 'lamswnehrtbxcpor'

        self.assertTrue(check(s1, s1))

        elapsed = (time.time() - t0)
        print(f"Test: {testname} took {elapsed} seconds.")


if __name__ == '__main__':
    unittest.main()