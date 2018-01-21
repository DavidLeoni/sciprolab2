import unittest
from exercise2 import *


class SquaresTest(unittest.TestCase):

    def test_0(self):
        self.assertEquals(squares(0),0)        

    def test_1(self):
        self.assertEquals(squares(1),1)        

    def test_2(self):
        self.assertEquals(squares(2),2)        

    def test_3(self):
        # 2^2 + 1^2
        self.assertEquals(squares(3),3)

    def test_4(self):
        # 2^2
        self.assertEquals(squares(4),1)

    def test_5(self):
        # 2^2  + 1^2
        self.assertEquals(squares(5),2)
        
    def test_13(self):
        # 3^2 + 2^2
        self.assertEquals(squares(13),2)

    def test_99(self):
        # 7^7 + 7^7 + 1
        self.assertEquals(squares(99),3)  
        