import unittest
import time
from CheckMapping import CheckMapping

checker = CheckMapping()
check = checker.check_mapping_actual

class TestCheckMapping(unittest.TestCase):

    def test_single_char(self):
        # testname= "Single"
        # t0 = time.time()

        self.assertTrue(check('a', 'b'))

        # elapsed = (time.time()-t0)
        # print(f"Test: {testname} took {elapsed} seconds.")

    def test_short_true(self):
        # testname= "Short True"
        # t0 = time.time()

        self.assertTrue(check('abc', 'def'))

        # elapsed = (time.time()-t0)
        # print(f"Test: {testname} took {elapsed} seconds.")

    # def test_short_false(self):
    #     # testname = "Short False"
    #     # t0 = time.time()
    #
    #     self.assertFalse(check('abc', 'bbb'))
    #     #
    #     # elapsed = (time.time() - t0)
    #     # print(f"Test: {testname} took {elapsed} seconds.")

    # def test_long_true(self):
    #     # testname = "Long True"
    #     # t0 = time.time()
    #     s1 = 'aaaabbbccdeffggghhhhiiiijjjkklmnnoopppqqqqrrrrsssttuvwwxxxyyyyzzzz'
    #     s2 = 'mnnoopppqqqqrrrrsssttuvwwxxxyyyyzzzzaaaabbbccdeffggghhhhiiiijjjkkl'
    #
    #     self.assertTrue(check(s1, s2))
    #
    #     # elapsed = (time.time() - t0)
    #     # print(f"Test: {testname} took {elapsed} seconds.")


    # def test_long_single_true(self):
    #     # testname = "Medium Single True"
    #     # t0 = time.time()
    #     s1 = 'abcdefghijklmnop'
    #     s2 = 'lamswnehrtbxcpor'
    #     #s2 = 'zyxwvutsrqponmlk'
    #     print(len(s1), len(s2))
    #
    #     self.assertFalse(check(s1, s2))
    #
    #     # elapsed = (time.time() - t0)
    #     # print(f"Test: {testname} took {elapsed} seconds.")

    def test_long_single_true(self):
        # testname = "Medium Single True"
        # t0 = time.time()
        s1 = 'abcdefghijklmnop'
        s2 = 'zyxwvutsrqponmlk'

        self.assertTrue(check(s1, s2))

    def test_1(self):
        s1 = "aaaabc"
        s2 = "bbbcbc"

        self.assertFalse(check(s1, s2))

    def test_2(self):
        s1 = "aaaabc"
        s2 = "bbbbcd"

        self.assertTrue(check(s1, s2))

    def test_3(self):
        s1 = "abc"
        s2 = "bcd"

        self.assertTrue(check(s1, s2))

    def test_4(self):
        s1 = "foo"
        s2 = "bar"

        self.assertFalse(check(s1, s2))

    def test_2(self):
        s1 = "bar"
        s2 = "foo"

        self.assertTrue(check(s1, s2))


if __name__ == '__main__':
    unittest.main()