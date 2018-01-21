from exercise3 import *
from algolab import gt
from algolab import GenericTreeTest

import unittest

class CountLeavesTest(GenericTreeTest):
    
    """
    a
    """
    def test1_a(self):
        ta = gt('a')
        
        self.assertEqual(ta.count_leaves(), 0)
    
    """
    a
    └b  <-- leaf
    """    
    def test2_a_b(self):
        ta = gt('a', gt('b'))
        self.assertEqual(ta.count_leaves(), 1)
 
    """
    a
    ├b  <-- leaf
    └c  <-- leaf
    """    
    def test3_a_bc(self):
        ta = gt('a', gt('b'), gt('c'))        
        self.assertEqual(ta.count_leaves(), 2)

    """
    a
    ├b
    |└c <-- leaf
    └d  <-- leaf
     
    """
    def test4_a_bc__d(self):
        ta = gt('a', gt('b', gt('c')), gt('d'))
        
        self.assertEqual(ta.count_leaves(), 2)

    """
    a
    ├b
    |└c <-- leaf
    └d 
     └e <-- leaf
    """
    def test5_a_bc__d_e(self):
        ta = gt('a', gt('b', gt('c')), gt('d', gt('e')))        
        self.assertEqual(ta.count_leaves(), 2)

    """
    a
    ├b
    |└c <-- leaf
    └d 
     └e 
      ├f <-- leaf
      └g <-- leaf
    """

    def test6_a_b_c__d_e_fg(self):
        ta = gt('a', gt('b', gt('c')), gt('d', gt('e', gt('f'), gt('g'))))
        
        self.assertEqual(ta.count_leaves(), 3)



class DetachLeavesTest(GenericTreeTest):
    
    """
    a
    """
    def test1_a(self):
        ta = gt('a')
        ta.detach_leaves()
        self.assertTreeEqual(ta, gt('a'))
    
    """
    a
    └b  <-- removed
    """    
    def test2_a_b(self):
        ta = gt('a', gt('b'))
        ta.detach_leaves()
        self.assertTreeEqual(ta, gt('a'))
 
    """
    a
    ├b  <-- removed
    ├c  <-- removed
    └d  <-- removed
    """    
    def test3_a_bcd(self):
        ta = gt('a', gt('b'), gt('c'), gt('d'))
        ta.detach_leaves()
        self.assertTreeEqual(ta, gt('a'))



    """
    a
    ├b
    |└c <-- removed
    └d  <-- removed
     
    """
    def test4_a_b_c__d(self):
        ta = gt('a', gt('b', gt('c')), gt('d'))
        ta.detach_leaves()
        self.assertTreeEqual(ta, gt('a', gt('b')))

    """
    a
    ├b  <-- removed
    └c   
     └d <-- removed
     
    """
    def test5_a_b__c_d(self):
        ta = gt('a', gt('b', gt('c')), gt('d'))
        ta.detach_leaves()
        self.assertTreeEqual(ta, gt('a', gt('b')))


    """
    a
    ├b
    |└c <-- removed
    └d 
     └e <-- removed
    """
    def test6_a_b_c__d_e(self):
        ta = gt('a', gt('b', gt('c')), gt('d', gt('e')))
        ta.detach_leaves()
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('d')))

    """
    a
    ├b
    |└c <-- removed
    └d 
     └e 
      ├f <-- removed
      └g <-- removed
    """

    def test7_a_b_c__d_e_fg(self):
        ta = gt('a', gt('b', gt('c')), gt('d', gt('e', gt('f'), gt('g'))))
        ta.detach_leaves()
        self.assertTreeEqual(ta, gt('a', gt('b'), gt('d', gt('e'))))

