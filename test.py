import unittest
from  re_engine import compile

from nfa import  simulate
class MyTestCase(unittest.TestCase):
    def test_re_engine(self):

        pat = compile("01*0")

        ans = simulate(pat, "000")

        self.assertEqual(ans == False, True)

        ans = simulate(pat, "00")
        self.assertEqual(ans == True, True)

        ans = simulate(pat, "01110")
        self.assertEqual(ans == True, True)

        ans = simulate(pat, "011101")
        self.assertEqual(ans == False, True)

    def test_match(self):
        pat = compile("(0|1)*001")

        ans = pat.match("00")
        self.assertEqual(ans == False, True)

        ans = pat.match("001")
        self.assertEqual(ans == True, True)

        ans = pat.match("11100")
        self.assertEqual(ans == False, True)

        ans = pat.match("0110011001")
        self.assertEqual(ans == True, True)


        ans = pat.match("010101010101010101")
        self.assertEqual(ans == False, True)

if __name__ == '__main__':
    unittest.main()
