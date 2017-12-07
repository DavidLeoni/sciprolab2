
"""
Test suite to fail all tree tests, so we see what happens when students make something wrong.

David Leoni - December 2017
"""


import sys
sys.path.append('exercises/trees/')

import unittest

from tree_solution import *
from algolab import gt, GenericTreeTest


class TreeFailTest(GenericTreeTest):

    def test_01_both_none(self):
        self.assertTreeEqual(None, None)
    
    def test_02_none_left(self):
        self.assertTreeEqual(None, gt('b'))

    def test_03_none_right(self):
        self.assertTreeEqual(gt('b'), None)
    
    def test_04_wrongClass(self):
        self.assertTreeEqual('hello', gt('a'))
    
    def test_05_data(self):
        self.assertTreeEqual(gt('a'), gt('b'))

    def test_06_big_tree(self):
        self.assertTreeEqual(gt('b', gt('hellooooooooooo', gt('d'), gt('e'))), gt('b', gt('e')))

    def test_07_number_tree(self):
        self.assertTreeEqual(gt(2, gt(3232323123123123, gt(3), gt(1))), gt(2, gt(1)))

    def test_08_mixed_tree(self):
        self.assertTreeEqual(gt(2, gt('hellllloooooooooooooo', gt(1234), gt(None))), gt('a', gt(1)))
        