from exercise3 import *
from algolab import dig, DiGraphTest
import unittest


class SpantreeTest(DiGraphTest):
    
    def test_empty(self):
        with self.assertRaises(Exception):
            dig().spantree('a')

    def test_not_found(self):
        with self.assertRaises(Exception):
            dig('a').spantree('b')


    def test_root(self):        
        self.assertEqual(dig('a', []).spantree('a'),
                          {'a': tuple()})
        self.assertEqual(dig('a', ['a']).spantree('a'),
                          {'a': tuple()})

    def test_one(self):        
        self.assertEqual(dig('a', ['b']).spantree('a'),
                          {'a': tuple(), 
                           'b': tuple('a')})


    def test_unreachable(self):        
        self.assertEqual(dig('a', [],
                              'b', []).spantree('a'),
                          {'a': tuple(), 
                          'b': tuple()})

    def test_triangle(self):        
        self.assertEqual(dig('a', ['b'],
                              'b', ['c'],
                              'c', ['a']).spantree('a'),
                          {'a': tuple(), 
                           'b': tuple('a'),
                           'c': ('a','b')})
        
    def test_complex(self):        
        self.assertEqual(dig('a', ['b','c'],
                              'b', ['d'],
                              'c', ['e']).spantree('a'),
                          {'a': tuple(), 
                           'b': tuple('a'),
                           'c': tuple('a'),
                           'd': ('a','b'),
                           'e' : ('a','c') })
