from exerciseB1 import *
import math
import unittest

class MaxRestTest(unittest.TestCase):

    def test_01_minus_inf(self):
        self.assertEqual(maxRest([],1),-math.inf)
        self.assertEqual(maxRest([2],1),-math.inf)
        self.assertEqual(maxRest([1],-1),-math.inf)
        self.assertEqual(maxRest([1],2),-math.inf)

    def test_02_zero(self):
        self.assertEqual(maxRest([],0),0)
        self.assertEqual(maxRest([1],0),0)
        self.assertEqual(maxRest([2],0),0)
        self.assertEqual(maxRest([1,1],0),0)
        self.assertEqual(maxRest([1,2],0),0)
        self.assertEqual(maxRest([2,1],0),0)

    def test_03_one(self):
        self.assertEqual(maxRest([1],1),1)
        self.assertEqual(maxRest([2],2),1)
        self.assertEqual(maxRest([3],3),1)

    def test_04_two(self):
        self.assertEqual(maxRest([1,1],1),1)
        self.assertEqual(maxRest([1,2],1),1)
        self.assertEqual(maxRest([2,1],1),1)
        self.assertEqual(maxRest([1,2],2),1)
        self.assertEqual(maxRest([2,1],2),1)
        self.assertEqual(maxRest([1,2],3),2)
        self.assertEqual(maxRest([2,1],3),2)

    def test_05_three(self):

        self.assertEqual(maxRest([1,1,2],2),2)
        self.assertEqual(maxRest([1,2,1],2),2)
        self.assertEqual(maxRest([2,1,1],2),2)
        self.assertEqual(maxRest([1,2,3],6),3)
        self.assertEqual(maxRest([1,3,2],6),3)
        self.assertEqual(maxRest([3,1,2],6),3)
        self.assertEqual(maxRest([2,1,3],6),3)
        self.assertEqual(maxRest([2,3,1],6),3)
        self.assertEqual(maxRest([3,2,1],6),3)

    def test_06_four(self):
        self.assertEqual(maxRest([2,2,3,1],4),2)
        self.assertEqual(maxRest([2,3,1,2],4),2)
        self.assertEqual(maxRest([3,2,1,2],4),2)
        self.assertEqual(maxRest([2,2,3,1],5),3)
        self.assertEqual(maxRest([2,3,1,2],5),3)
        self.assertEqual(maxRest([3,2,1,2],5),3)

    def test_06_six(self):
        self.assertEqual(maxRest([2,1,5,2,2,5],7) , 4)
        self.assertEqual(maxRest([1,2,5,5,2,2],7) , 4)
