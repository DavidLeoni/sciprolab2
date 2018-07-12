import unittest
from exerciseB1 import *

class TestStairs(unittest.TestCase):

    def test_neg(self):
        self.assertEqual(stairs(-1),0)
        self.assertEqual(stairs(-2),0)

    def test_zero(self):
        self.assertEqual(stairs(0),1)

    def test_one(self):
        self.assertEqual(stairs(1),1)  # 1

    def test_two(self):
        self.assertEqual(stairs(2),2)  # 1 1, 2

    def test_three(self):
        self.assertEqual(stairs(3),4)   # 1 1 1 , 2 1, 1 2 , 3

    def test_four(self):
        self.assertEqual(stairs(4),8)   # 1 1 1 1, 
                                        # 2 1 1 , 1 2 1, 1 1 2
                                        # 2 2
                                        # 3 1, 1 3
                                        # 4

    def test_five(self):
        self.assertEqual(stairs(5),15)  # 1 1 1 1 1,  
                                        # 2 1 1 1,    1 2 1 1, 1 1 2 1, 1 1 1 2
                                        # 2 2 1,      2 1 2,   1 2 2 
                                        # 3 1 1,      1 3 1,   1 1 3,   
                                        # 3 2,        2 3 
                                        # 4 1,        1 4
                                        


