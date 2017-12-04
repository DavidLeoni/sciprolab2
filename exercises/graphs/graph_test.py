from graph import *
from algolab import dig, DiGraphTest
import unittest


class HasEdgeTest(DiGraphTest):
    
    def test_has_edge(self):
        self.assertTrue(dig('a',['b']).has_edge('a','b'))    
        self.assertFalse(dig('a',['b']).has_edge('a','a'))    
        self.assertTrue(dig('a',['b'],
                            'a',['c']).has_edge('a','c'))
                            
        with self.assertRaises(Exception):
            self.assertTrue(dig('a',['b']).has_edge('a','c'))

            
        
class FullGraphTest(DiGraphTest):
    
    def test_full_graph(self):
        self.assertDiGraphEqual(full_graph([]),
                                dig())
        self.assertDiGraphEqual(full_graph(['a']),
                                dig('a', ['a']))
        self.assertDiGraphEqual(full_graph(['a','b']), 
                                dig('a',['a','b'],
                                    'b',['a','b']))

class DagTest(DiGraphTest):        
    
    def test_dag(self):
        self.assertDiGraphEqual(dag([]), dig())
        self.assertDiGraphEqual(dag(['a']), dig('a', []))
        self.assertDiGraphEqual(dag(['a', 'b']), dig('a', ['b']))
        self.assertDiGraphEqual(dag(['a','b','c']),
                                dig('a',['b','c'],
                                    'b',['c']))

class ListGraphTest(DiGraphTest):        
    
    def test_list_graph(self):
        with self.assertRaises(Exception):
            list_graph(-4)
                    
        self.assertEquals(dig(), list_graph(0))
        self.assertEquals(dig(1,[]), list_graph(1))
        self.assertEquals(dig(1,[2],2,[3]), list_graph(3))
        
class StarGraphTest(DiGraphTest):        

    def test_star_graph(self):
        with self.assertRaises(Exception):
            star_graph(-4)
        self.assertDiGraphEqual(star_graph(0),
                                dig())
        self.assertDiGraphEqual(star_graph(1),
                                dig(1,[]))      
        
        self.assertDiGraphEqual(star_graph(2),
                                dig(1, [2]))
        self.assertDiGraphEqual(star_graph(3),
                                dig(1, [2,3]))
        self.assertDiGraphEqual(star_graph(4),
                                dig(1, [2,3,4]))
        

        
class TestRemoveVertex(DiGraphTest):
    
    def test_remove_vertex_empty(self):
        with self.assertRaises(Exception):
            dig().remove_vertex('a')
        
    def test_remove_vertex_two(self):        
        g = dig('a', ['b'],
                'b', ['a'])
        
        g.remove_vertex('a')
        self.assertDiGraphEqual(g, dig('b', []))
        
        g.remove_vertex('b')
        self.assertDiGraphEqual(g, dig())

    def test_remove_vertex_self(self):        
        g = dig('a', ['a'],
                'b', ['a', 'b'])
        
        g.remove_vertex('b')
        self.assertDiGraphEqual(g, dig('a', ['a']))
        
        g.remove_vertex('a')
        self.assertDiGraphEqual(g, dig())

class ReverseTest(DiGraphTest):
    
    def test_reverse_empty(self):
        g = dig()
        g.reverse()
        self.assertDiGraphEqual(dig(), g)
        
    def test_reverse_return_none(self):
        self.assertReturnNone(dig().reverse(), 'reverse')
        self.assertReturnNone(dig('a', ['b']).reverse(), 'reverse')                

    def test_reverse_self(self):
        g = dig('a', ['a'])
        g.reverse()
        self.assertDiGraphEqual(g, g)
        
    def test_reverse_bipartite(self):
        g = dig('a', ['c'],
                'b', ['d'])
        g.reverse()
        self.assertDiGraphEqual(g, dig('c', ['a'],
                                    'd', ['b']))

    def test_reverse_star(self):
        g = dig('a', ['b','c','d'])
        g.reverse()
        self.assertDiGraphEqual(g, dig('b', ['a'],
                                    'c', ['a'],
                                    'd', ['a']))
        g.reverse()
        self.assertEqual(g, dig('a', ['b','c','d']))

        
class HasSelfLoopsTest(DiGraphTest):       
        
    def test_has_self_loops_empty(self):        
        self.assertFalse(dig().has_self_loops())

    def test_has_self_loops_one(self):        
        self.assertFalse(dig('a',[]).has_self_loops())
        self.assertTrue(dig('a',['a']).has_self_loops())

    def test_has_self_loops_two(self):        
        self.assertFalse(dig('a',[]).has_self_loops())
        self.assertTrue(dig('a',['b', 'a']).has_self_loops())
        self.assertFalse(dig('a',['b'],
                            'b',['a']).has_self_loops())


class RemoveSelfLoopTest(DiGraphTest):
        
    def test_remove_self_loops_empty(self):
        g = dig()
        g.remove_self_loops()
        self.assertDiGraphEqual(g, dig())

    def test_remove_self_loops_no_loops(self):
        g = dig('a',[])
        g.remove_self_loops()
        self.assertDiGraphEqual(g, dig('a',[]))

    def test_remove_self_loops_complex(self):
        g = dig('a',['a','b'],
                 'b',['c', 'b'])
        g.remove_self_loops()
        self.assertDiGraphEqual(g,
                                dig('a', ['b'],
                               'b', ['c']))


class DistancesTest(DiGraphTest):
    
    def test_distances_empty(self):
        with self.assertRaises(Exception):
            dig().distances('a')

    def test_distances_not_found(self):
        with self.assertRaises(Exception):
            dig('a').distances('b')


    def test_distances_root(self):        
        self.assertEquals(dig('a', []).distances('a'),
                          {'a': 0})
        self.assertEquals(dig('a', ['a']).distances('a'),
                          {'a': 0})

    def test_distances_one(self):        
        self.assertEquals(dig('a', ['b']).distances('a'),
                          {'a': 0, 
                           'b': 1})


    def test_distances_unreachable(self):        
        self.assertEquals(dig('a', [],
                              'b', [],).distances('a'),
                          {'a': 0, 
                          'b': -1})

    def test_distances_triangle(self):        
        self.assertEquals(dig('a', ['b'],
                              'b', ['c'],
                              'c', ['a']).distances('a'),
                          {'a': 0, 
                           'b': 1,
                           'c': 2})
        
    def test_distances_square(self):        
        self.assertEquals(dig('a', ['b','c'],
                              'b', ['d'],
                              'c', ['d']).distances('a'),
                          {'a': 0, 
                           'b': 1,
                           'c': 1,
                           'd': 2})

            