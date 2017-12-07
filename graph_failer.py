"""
Test suite to fail all graph tests, so we see what happens when students do something wrong.

David Leoni - December 2017
"""


import sys
sys.path.append('exercises/graphs/')

from graph_solution import *
from algolab import dig, DiGraphTest 

class GraphFailTest(DiGraphTest):

    def test_01_both_none(self):
        self.assertDiGraphEqual(None, None)
    
    def test_02_none_left(self):
        self.assertDiGraphEqual(None, dig('b',[]))

    def test_03_none_right(self):
        self.assertDiGraphEqual(dig('b',[]), None)
    
    def test_04_wrongClass(self):
        self.assertDiGraphEqual('hello', dig('a',[]))
    
    def test_05_data(self):
        self.assertDiGraphEqual(dig('a',[]), dig('b',[]))

    def test_06_big_graph(self):
        self.assertDiGraphEqual(dig('b', ['hellooooooooooo', 'd']),dig('b',['woooooooooooooorld']))

    def test_07_number_graph(self):
        self.assertDiGraphEqual(dig(3, [2, 432342342343243234234234232, 32323]),dig(3,[129894343412111, 3]))
        
        
    def test_08_mixed_big_graph(self):
        self.assertDiGraphEqual(dig('a', [2, 432342342343243234234234232, 'ammmmmmmmmaazzzzaa']),dig('a',[2, 129894343412111], None, [3]))

    def test_09_mixed_small_graph(self):
        self.assertDiGraphEqual(dig('a', [2, 4, 'c']),dig('a',[2, 1], None, [3]))
        
        