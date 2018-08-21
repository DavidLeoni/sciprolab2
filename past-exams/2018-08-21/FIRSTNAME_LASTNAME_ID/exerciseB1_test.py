import unittest
from exerciseB1 import *


class TesStock(unittest.TestCase):

    def test_1_stock(self):
        self.assertEqual(stock([1]), 0 )


    def test_2_stock(self):
        self.assertEqual(stock([2]), 0 )


    def test_5_stock(self):
        self.assertEqual(stock([5]), 0 )


    def test_7_stock(self):
        self.assertEqual(stock([7]), 0 )


    def test_8_stock(self):
        self.assertEqual(stock([8]), 0 )


    def test_5_5_stock(self):
        self.assertEqual(stock([5, 5]), 0 )


    def test_5_8_stock(self):
        self.assertEqual(stock([5, 8]), 3 )


    def test_8_5_stock(self):
        self.assertEqual(stock([8, 5]), 0 )


    def test_8_8_stock(self):
        self.assertEqual(stock([8, 8]), 0 )


    def test_5_5_5_stock(self):
        self.assertEqual(stock([5, 5, 5]), 0 )


    def test_5_5_7_stock(self):
        self.assertEqual(stock([5, 5, 7]), 4 )


    def test_5_5_8_stock(self):
        self.assertEqual(stock([5, 5, 8]), 6 )


    def test_5_7_5_stock(self):
        self.assertEqual(stock([5, 7, 5]), 2 )


    def test_5_7_7_stock(self):
        self.assertEqual(stock([5, 7, 7]), 2 )


    def test_5_7_8_stock(self):
        self.assertEqual(stock([5, 7, 8]), 4 )


    def test_5_8_5_stock(self):
        self.assertEqual(stock([5, 8, 5]), 3 )


    def test_5_8_7_stock(self):
        self.assertEqual(stock([5, 8, 7]), 3 )


    def test_5_8_8_stock(self):
        self.assertEqual(stock([5, 8, 8]), 3 )


    def test_7_5_5_stock(self):
        self.assertEqual(stock([7, 5, 5]), 0 )


    def test_7_5_7_stock(self):
        self.assertEqual(stock([7, 5, 7]), 2 )


    def test_7_5_8_stock(self):
        self.assertEqual(stock([7, 5, 8]), 4 )


    def test_7_7_5_stock(self):
        self.assertEqual(stock([7, 7, 5]), 0 )


    def test_7_7_7_stock(self):
        self.assertEqual(stock([7, 7, 7]), 0 )


    def test_7_7_8_stock(self):
        self.assertEqual(stock([7, 7, 8]), 2 )


    def test_7_8_5_stock(self):
        self.assertEqual(stock([7, 8, 5]), 1 )


    def test_7_8_7_stock(self):
        self.assertEqual(stock([7, 8, 7]), 1 )


    def test_7_8_8_stock(self):
        self.assertEqual(stock([7, 8, 8]), 1 )


    def test_8_5_5_stock(self):
        self.assertEqual(stock([8, 5, 5]), 0 )


    def test_8_5_7_stock(self):
        self.assertEqual(stock([8, 5, 7]), 2 )


    def test_8_5_8_stock(self):
        self.assertEqual(stock([8, 5, 8]), 3 )


    def test_8_7_5_stock(self):
        self.assertEqual(stock([8, 7, 5]), 0 )


    def test_8_7_7_stock(self):
        self.assertEqual(stock([8, 7, 7]), 0 )


    def test_8_7_8_stock(self):
        self.assertEqual(stock([8, 7, 8]), 1 )


    def test_8_8_5_stock(self):
        self.assertEqual(stock([8, 8, 5]), 0 )


    def test_8_8_7_stock(self):
        self.assertEqual(stock([8, 8, 7]), 0 )


    def test_8_8_8_stock(self):
        self.assertEqual(stock([8, 8, 8]), 0 )

    def test_four(self):
        self.assertEqual(stock([1,7,3,6]), 9 )

    def test_six(self):
        self.assertEqual(stock([7,1,2,5,3,1]), 7 )
