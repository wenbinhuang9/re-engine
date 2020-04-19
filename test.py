import unittest
from  re_engine import compile, matchfull, match, search, findAll

from nfa import  simulate
class MyTestCase(unittest.TestCase):


    def test_match_full(self):
        pat = compile("(0|1)*001")

        ans = matchfull(pat, "00")
        self.assertEqual(ans == None, True)

        ans = matchfull(pat, "001")
        self.assertEqual(ans !=None, True)

        ans = matchfull(pat, "11100")
        self.assertEqual(ans == None, True)

        ans = matchfull(pat, "0110011001")
        self.assertEqual(ans != None , True)

        ans = matchfull(pat, "010101010101010101")
        self.assertEqual(ans == None, True)

    def test_match(self):
        pat = compile("(0|1)*001")

        ans = match(pat, "001000")
        self.assertEqual(ans != None, True)

        ans = match(pat, "00000000")
        self.assertEqual(ans == None, True)

    def test_search(self):
        pat = compile("101*01")

        ans = search(pat, "100100")
        print (ans)
        self.assertEqual(ans != None, True)

        ans = search(pat, "00100100")
        print ans
        self.assertEqual(ans != None, True)

    def test_findall(self):
        pat = compile("101*01")

        ans = findAll(pat, "1001101010001001")
        correct_ans = ['1001', '10101', '1001']

        self.assertEqual(all([correct_ans[i] == item for i, item in enumerate(ans.matchedList)]), True)

if __name__ == '__main__':
    unittest.main()
