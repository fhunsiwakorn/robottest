from cal import sum,minus,multiply,divide
import unittest


class Test_Calculator(unittest.TestCase):
    def testSumFunction(self):
        self.assertEqual(sum(1,2),3) 

    def testMinusFunction(self):
        self.assertEqual(minus(10,0),10) 

    def testMultiplyFunction(self):
        self.assertEqual(multiply(2,2),4) 

    def testDivideFunction(self):
        self.assertEqual(divide(6,3), 2) 