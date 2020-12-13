from calgrade import calGrade
import unittest


class Test_Calculator(unittest.TestCase):
    def testSumFunction(self):
        self.assertEqual(calGrade(80), 'A')

    # def testMinusFunction(self):
    #     self.assertEqual(calGrade(70))

    # def testMultiplyFunction(self):
    #     self.assertEqual(calGrade(80))

    # def testDivideFunction(self):
    #     self.assertEqual(calGrade(65))