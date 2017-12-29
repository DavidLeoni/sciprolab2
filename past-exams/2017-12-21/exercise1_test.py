from exercise1 import *
import unittest

def is_env_working():
    """ Don't modify this function"""
    return "yes"


class EnvWorkingTest(unittest.TestCase):
    """ Just to test you can run tests.  """
    
    def test_env_working(self):
        """ This test should always pass."""
        self.assertEqual(is_env_working(), "yes")


class LopalTest(unittest.TestCase):
    
    def test_01_empty(self):
        self.assertEqual(lopal(""),0) # second is the expected value

    def test_02_one(self):
        self.assertEqual(lopal("A"),1) 

    def test_03_two(self):
        self.assertEqual(lopal("AA"),2) 

    def test_04_three(self):
        self.assertEqual(lopal("ABA"),3) 
        
    def test_05_sub_two(self):
        self.assertEqual(lopal("CABBC"),2) 
        
    def test_06_sub_long(self):
        self.assertEqual(lopal("BUBBASEESABANANA"),8)

    def test_07_pal_long(self):
        self.assertEqual(lopal("AFISICACISIFA"),13)
        