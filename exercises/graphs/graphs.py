import unittest
import pprint
from Queue import Queue
import traceback

#PrettyPrint(indent=4)

pp = pprint.PrettyPrinter(indent=4).pprint
pformat = pprint.PrettyPrinter(indent=4).pformat

class VertexLog:
    """ Represents the visit log a single DiGraph vertex
    
        This class is very simple and doesn't even have getters methods. 

        You can just access fields by using the dot:

            print vertex_log.discovery_time

        and set them directly:

            vertex_log.finish_time = 5
        
        If you want, an instances you can set your own fields:
        
            vertex_log.my_own_field = "whatever"
    """
    
    def __init__(self, vertex):
        self.vertex = vertex
        self.discovery_time = -1
        self.finish_time = -1
        self.parent = None              
        
    def __repr__(self):        
        return pformat(vars(self))
       
class Visit:
    """ The visit of a DiGraph visit sequence. 
    
    """

    def __init__(self):
        """ Creates a Visit """
            
        self._logs = {}
        

    def is_discovered(self, vertex):
        """ Returns true if given vertex is present in the log and 
            has discovery_time != -1
        """
        return vertex in self._logs and self._logs[vertex].discovery_time != -1

    def log(self, vertex):
        """ Returns the log of the given vertex. 
        
            If there is no existing log, a new one will be created and returned
        """        
        
        if not vertex in self._logs:
            self._logs[vertex] = VertexLog(vertex)
        
        return self._logs[vertex]
        
    def logs(self, 
             sort_by=lambda log: log.discovery_time, 
             descendant=False,
             get_all=False):
        """ Returns an array with sequence of discovered VertexLogs, sorted by discovery time.

            Optionally, they can be sorted by:
            - a custom field using 'sort_by' parameter 
            - in descendent order with 'descendant' parameter.
            
            By default only discovered vertex logs are returned:
             to get all, use get_all=True
        """
        if get_all:
            ret = self._logs.values()            
        else:
            ret = filter(lambda log: log.discovery_time > -1, self._logs.values())

        ret.sort(key= sort_by, reverse= descendant)
        return ret
        
    def verteces(self, 
                 sort_by=lambda log: log.discovery_time, 
                 descendant=False,
                 get_all=False):
        """ Returns an array with sequence of the discovered VertexLogs, sorted by discovery time.

            Optionally, they can be sorted by:
            - a custom field using 'sort_by' parameter 
            - in descendent order with 'descendant' parameter.
            
            By default only discovered vertex logs are returned:
             to get all, use get_all=True
        """
        return map(lambda vertex_log:vertex_log.vertex,                                      
                   self.logs(sort_by=sort_by, 
                             descendant=descendant,
                             get_all=get_all))

    
    def last_time(self):
        """ Return the maximum time found among discovery and finish times.
        
            If no node was visited, returns zero.        
        """        
        
        max_time = 0
        for log in self._logs.values():
            if log.discovery_time > max_time:
               max_time = log.discovery_time 
            if log.finish_time > max_time:
               max_time = log.finish_time 
        return max_time                
                    
    def __str__(self):
        return "Visit:\n" + pformat(self.logs())            
        
class DiGraph:
    """ A simple graph data structure, represented as a dictionary of adjacency lists
    
        Verteces can be of any type, to keep things simple in this data model they coincide with their labels.
        Adjacency lists hold the target verteces. 
        Attempts to add duplicate targets will be silently ignored.
        
        For shorthand construction, see separate dig() function
    """
            
    def __init__(self):
        # The class just holds the dictionary _edges: as keys it has the verteces, and 
        # to each vertex associates a list with the verteces it is linked to.
        self._edges = {}
        
    def add_vertex(self, vertex):
        """ Adds vertex to the DiGraph. A vertex can be any object.
            
            If the vertex already exist, does nothing.
        """
        if vertex not in self._edges:            
            self._edges[vertex] = []
    
    def verteces(self):
        """ Returns a set of the graph verteces. Verteces can be any object. """
        
        # Note dict keys() return a list, not a set. Bleah.  
        # See http://stackoverflow.com/questions/13886129/why-does-pythons-dict-keys-return-a-list-and-not-a-set
        return set(self._edges.keys()) 
        
    def has_vertex(self, vertex):
        """ Returns true if graph contains given vertex. A vertex can be any object. """
        return vertex in self._edges

            
    def add_edge(self, vertex1, vertex2):
        """ Adds an edge to the graph, from vertex1 to vertex2
        
            If verteces don't exist, raises an Exception.
            If there is already such an edge, exits silently.            
        """
        
        if not vertex1 in self._edges:
            raise Exception("Couldn't find source vertex: " + str(vertex1))

        if not vertex2 in self._edges:
            raise Exception("Couldn't find target vertex: " + str(vertex2))        
            
        if not vertex2 in self._edges[vertex1]:
            self._edges[vertex1].append(vertex2)

    def adj(self, vertex):
        """ Returns the verteces adjacent to vertex. 
            
            NOTE: verteces are returned in a NEW list.
            Modifying the list will have NO effect on the graph!
        """
        if not vertex in self._edges:
            raise Exception("Couldn't find a vertex " + str(vertex))
        
        return self._edges[vertex][:]

    def is_empty(self):
        """  A DiGraph for us is empty if it has no verteces and no edges """
        
        return len(self._edges) == 0

      
    def __eq__(self, other):
        """ !!!   NOTE: although we represent the set with adjanceny lists, for __eq__
            graph dig('a', ['b','c']) is considered equals to a graph dig('a', ['c', 'b']) !!! 
        """
            
        if not isinstance(other, DiGraph):
            return False            
        
        if self.verteces() != other.verteces():
            return False
        
        
        for source in self._edges:            
            if set(self._edges[source]) != set(other._edges[source]):
                return False
        
        return True
        
    def __ne__(self, other):
        """ not equal. 
            For the necessity of implementing it, see this: http://jcalderone.livejournal.com/32837.html 
        """
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result         

    def __str__(self):
        """ Returns a string representation like the following:
        
            >>> print gr('a',['b','c', 'd'],
                         'b', ['b'],
                         'c', ['a'])

            a: [b,c]
            b: [b]
            c: [a]         
            d: []
        
        """
        
        if (len(self._edges) == 0):
            return "\nDiGraph()" 
        
        max_len=0
        
        sorted_verteces = sorted(self._edges.keys())
        
        for source in self._edges:
            max_len = max(max_len, len(str(source)))
        
        strings = ["\n"]
        
        for source in sorted_verteces:
            
            strings.append(str(source).ljust(max_len))
            strings.append(': ')            
            strings.append(str(self._edges[source]))
            
            strings.append('\n')
        
        return ''.join(strings)       
        
    def __repr__(self):              
        return self.__str__()        

    def dfs(self, source, visit=None):
        """ Performs a simple depth first search on the graph
            
            Returns a Visit of the visited nodes. If the graph is empty, raises an Exception.
            Optionally, you can pass the initial visit trace. 
        """
        
        if self.is_empty():
            raise Exception("Cannot perform DFS on an empty graph!")
        
        if visit == None:
            visit = Visit()            
        
        # we just discovered the vertex           
        source_log = visit.log(source)
        source_log.discovery_time = visit.last_time() + 1
        
        for neighbor in self.adj(source): 
            if not visit.is_discovered(neighbor):
                
                visit.log(neighbor).parent = source        
            
                self.dfs(neighbor, visit)                
                
        source_log.finish_time = visit.last_time() + 1    
        
        return visit

        
    def bfs(self, source):
        """ Performs a simple breadth first search in the graph, starting from 
            provided source vertex.
            
            Returns a Visit of the discovered nodes.
            NOTE: it stores discovery but not finish times.
            
            If source is not in the graph, raises an Exception                         
        """
        
        if self.is_empty():
            raise Exception("Cannot perform BFS on an empty graph!")
        
        if not source in self.verteces():
            raise Exception("Can't find vertex:" + str(source))
        
        visit = Visit()  
        
        queue = Queue()        
        queue.put(source)

        while not queue.empty():
            vertex = queue.get()
                        
            if not visit.is_discovered(vertex):
                # we just discovered the node
                visit.log(vertex).discovery_time = visit.last_time() + 1
            
                for neighbor in self.adj(vertex):                                
                    neighbor_log = visit.log(neighbor)
                    if neighbor_log.parent == None and neighbor != source:
                        neighbor_log.parent = vertex
                    queue.put(neighbor)                    
        
        return visit            


    def has_edge(self, source, target):
        """  Returns True if there is an edge between source vertex and target vertex. 
             Otherwise returns False.

            If either source, target or both verteces don't exist raises an Exception.
        """
        
        raise Exception("TODO IMPLEMENT ME!")                             

    def remove_vertex(self, vertex):
        """ Removes the provided vertex  and returns it
            
            If the vertex is not found, raises an Exception.
        """
                
        raise Exception("TODO IMPLEMENT ME!")

    
    def reverse(self):
        """ Reverses the direction of all the edges 
        
            Note this one changes in-place the graph: does **not** create a new instance
            and does *not* return anything !!        
        """
           
        raise Exception("TODO IMPLEMENT ME!")
    
    def has_self_loops(self):
        """ Returns True if the graph has any self loop (a.k.a. cap), False otherwise """
        
        raise Exception("TODO IMPLEMENT ME!")
        
    def remove_self_loops(self):
        """ Removes all of the self-loops edges (a.k.a. caps) 
            
            NOTE: Removes just the edges, not the verteces!
        """


        raise Exception("TODO IMPLEMENT ME!")
                
    def distances(self, source):
        """ 
        Returns a dictionary where the keys are verteces, and each vertex v is associated
        to the *minimal* distance in number of edges required to go from the source 
        vertex to vertex v. If node is unreachable, the distance will be -1
        
        Source has distance zero from itself
        Verteces immediately connected to source have distance one.

        if source is not a vertex, raises an Exception
        
        HINT: to implement this, copy and edit either dfs or bfs. Question: which one ?
        """        
       
        raise Exception("TODO IMPLEMENT ME!")        



def str_compare_digraphs(actual, expected):
    """ Returns a string representing a comparison side by side 
        of the provided digraphs
    
    """

    if actual == None and expected == None:
        return "Both graphs are None."

    if (actual == None) ^ (expected == None):
        if actual == None:
            what = ""
        else:
            what = "NOT"
        return "ACTUAL GRAPH IS " + what + " None ! " +"\n\nACTUAL: \n" + str(actual)  +"\n\nEXPECTED: \n" + str(expected) 


    if actual.is_empty() ^ expected.is_empty():
        if actual.is_empty():
            what = ""
        else:
            what = "NOT"
            
        return " ACTUAL GRAPH IS " + what + " EMPTY ! " +"\n\nACTUAL: \n" + str(actual)  +"\n\nEXPECTED: \n" + str(expected) 


    max_len1_keys = 0    
    for source in actual.verteces():
        max_len1_keys = max(max_len1_keys, len(str(source)+": " ))

    
    max_len1 = 0    
    for line in str(actual).split("\n"):
        max_len1 = max(max_len1, len(line))
    max_len1 = max(max_len1, len("ACTUAL"))

    max_len2_keys = 0    
    for source in expected.verteces():
        max_len2_keys = max(max_len2_keys, len(str(source)+": " ))
    
            
    max_len2 = 0    
    for line in str(expected).split("\n"):
        max_len2 = max(max_len2, len(line))
    max_len2 = max(max_len1, len("EXPECTED"))
    
    strings = []
    
    vs = sorted(set(actual.verteces()).union( expected.verteces()))

    strings = []

    dist = 2
    dist2 = - max_len2_keys
    
    strings.append((" " * max_len1_keys + "ACTUAL").ljust(max_len1 + dist))
    strings.append("  EXPECTED\n")
    
    for vertex in vs:
                
        strings.append(str(vertex))
        strings.append(': ')
                
        if vertex in actual.verteces():
            strings.append(str(actual.adj(vertex)).ljust(max_len1 + dist))
        else:
            strings.append("--" + " " * (max_len1 + dist - 2))
            
        if vertex in expected.verteces():            
            strings.append(str(expected.adj(vertex)).ljust(max_len2 + dist2))
        else:
            strings.append("--" + " " * (max_len2 + dist2 - 2))
        
        if (not vertex in actual.verteces()
            or not vertex in expected.verteces()
            or set(actual.adj(vertex)) != set(expected.adj(vertex))):
            strings.append("  <---- DIFFERENT ! ")
        
        strings.append("\n")
            
    return ''.join(strings)

  

def dig(*args):
    """ Shorthand to construct a DiGraph with provided arguments
    
        To use it, provide pairs source vertex / target verteces list like in the following examples:
        
        >>> print dig()        
        
        DiGraph()
        
        >>> print dig('a',['b','c'])
                
        a: [b,c]
        b: []
        c: []
        
        >>> print dig('a',['b','c'],
                     'b', ['b'],
                     'c', ['a'])
                
        a: [b,c]
        b: [b]
        c: [a]                
        
    """
    
    g = DiGraph()
        
    if len(args) % 2 == 1:
        raise Exception("Number of arguments must be even! You need to provide"
                    + " vertex/list pairs like 'a',['b', 'c'], b, ['d'], ... !")

    i = 1        
    for a in args:
        
        if i % 2 == 1:
            vertex = a
            g.add_vertex(vertex)            
            
        else:
            try:
                iter(a)
            except TypeError:
                raise Exception('Targets of ' + str(vertex) + ' are not iterable: ' + str(a) )
            for target in a:
                if not g.has_vertex(target):
                    g.add_vertex(target)
                g.add_edge(vertex, target)
        i += 1
    
    return g
    
    
    
def gen_graphs(n):    
    """ Returns a list with all the possible 2^(n^2) graphs of size n 
    
        Verteces will be identified with numbers from 1 to n 
    """    

    def gen_bits(n):
        """  Generates a sequence of 2^(n^2) lists, each of n^2 0 / 1 ints  """
                        
        bits = n*n;    
        nedges = 2**bits    
        
        ret = []
        for i in range(0, nedges):
                    
            right = [int(x) for x in bin(i)[2:]]
            lst = ([0] * (bits - len(right)))
            lst.extend(right)
    
            ret.append(lst)
        return ret

    if n == 0:
        return [DiGraph()]
        
    i = 0
    
    ret = []

    for lst in gen_bits(n):
        
        g = DiGraph()
        for j in range(1, n+1):
            g.add_vertex(j)
        
        source = 0
        for b in lst:            
            if i % n == 0:
                source += 1
            if b:
                g.add_edge(source, (i % n) + 1)
            i += 1
        ret.append(g)
    return ret
     
GRAPHS_3 = gen_graphs(3)


def full_graph(verteces):
    """ Returns a DiGraph which is a full graph with provided verteces list.
    
        In a full graph all verteces link to all other verteces (including themselves!).
    """
    
    raise Exception("TODO IMPLEMENT ME!")
    
    
def dag(verteces):
    """ Returns a DiGraph which is DAG (Directed Acyclic Graph) made out of provided verteces list
    
        Provided list is intended to be in topological order.
        NOTE: a DAG is ACYCLIC, so caps (self-loops) are not allowed !!
    """

    raise Exception("TODO IMPLEMENT ME!")
    
def list_graph(n):
    """ Return a graph of n verteces displaced like a 
        monodirectional list:  1 -> 2 -> 3 -> ... -> n 
        
        Each vertex is a number i, 1 <= i <= n  and has only one edge connecting it
        to the following one in the sequence        
        If n = 0, return the empty graph.
        if n < 0, raises an Exception.
    """    
        
    raise Exception("TODO IMPLEMENT ME!")
    
def star_graph(n):
    """ Returns graph which is a star with n nodes 

        First node is the center of the star and it is labeled with 1. This node is linked 
        to all the others. For example, for n=4 you would have a graph like this:
        
                3
                ^
                |    
           2 <- 1 -> 4           
           
        If n = 0, the empty graph is returned
        If n < 0, raises an Exception           
    """    
    
    raise Exception("TODO IMPLEMENT ME!")    
    
class VisitTest(unittest.TestCase):
    
    def test_log(self):
        """ Checks it doesn't explode with non-existing verteces """
        self.assertEqual(-1, Visit().log('a').discovery_time)
        self.assertEqual(-1, Visit().log('a').finish_time)

    def test_verteces(self):        
        self.assertEqual([], Visit().verteces())
        
        visit = Visit()
        visit.log('a')
        self.assertEqual([], visit.verteces())
        self.assertEqual(['a'], visit.verteces(get_all=True))
        visit.log('a').discovery_time = 1
        self.assertEqual(['a'], visit.verteces())
        visit.log('b').discovery_time = 2
        self.assertEqual(['a', 'b'], visit.verteces())
        #  descendant=False, get_all=False):
        self.assertEqual(['b', 'a'], visit.verteces(descendant=True))
        self.assertEqual(['b', 'a'], visit.verteces(descendant=True))
        
        visit.log('a').finish_time = 4
        visit.log('b').finish_time = 3
        self.assertEqual(['b', 'a'], visit.verteces(sort_by=lambda log:log.finish_time))
        
    def test_str(self):
        visit = Visit()
        visit.log('z').discovery_time = 1        
        self.assertTrue('z' in str(visit))
        
        
class DiGraphTest(unittest.TestCase):    
    
    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEqual(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! Instead you are returning " + str(ret))

    
    def assertDiGraphEqual(self, actual, expected,  msg=None):                    
        if not expected == actual:            
            if msg == None:
                the_msg = "Graphs are different:"
            else:
                the_msg = msg
            raise AssertionError(the_msg + " \n\n" + str_compare_digraphs(actual, expected) )
    
    def assertSubset(self, set1, set2):
        """ Asserts set1 is a subset of set2 """
        
        if not set1.issubset(set2):
            raise AssertionError(str(set1) + " is not a subset of " + str(set2))
    
    def raise_graph(self, exception, graph, visit):
        """ Emulates reraising an exception for a given graph visit """
                        
        raise Exception(traceback.format_exc(exception)
             +"\n Failed graph was: \n" + str(graph)
             +"\n Failed graph visit was: \n" + str(visit))

    def test_adj(self):
        self.assertEqual(dig('a', []).adj('a'), 
                         [])
        self.assertEqual(dig('a', ['b']).adj('a'),
                         ['b'])
        self.assertEqual(dig('a', ['b', 'c']).adj('a'),
                         ['b', 'c'])
        g = dig('a', ['b'])
        lst = g.adj('a')
        lst[0] = 'c'
        self.assertEqual(['b'], g.adj('a'))
        
    def test_has_edge(self):
        self.assertTrue(dig('a',['b']).has_edge('a','b'))    
        self.assertFalse(dig('a',['b']).has_edge('a','a'))    
        self.assertTrue(dig('a',['b'],
                            'a',['c']).has_edge('a','c'))
                            
        with self.assertRaises(Exception):
            self.assertTrue(dig('a',['b']).has_edge('a','c'))

    def test_eq(self):
        
        self.assertEqual(dig('a', ['b','c']),
                         dig('a', ['c', 'b']))        
                                         
        self.assertTrue(dig('a', ['b','c']) == dig('a', ['c', 'b']))                         
        self.assertFalse(dig('a', ['b']) == dig('a', ['c', 'b']))                         
    
    def test_str(self):
        self.assertTrue("DiGraph()" in str(dig()))
        self.assertTrue("x" in str(dig('x',['y'])))
        self.assertTrue("y" in str(dig('x',['y'])))
        self.assertEquals(set(['x','y']), dig('x',['y']).verteces())
        self.assertEquals(set(['x','y','z','w', 'z']),
                          dig('x',['y'], 'z', ['w','x']).verteces())
       
                
    def test_gen_graphs(self):
        
        gs0 = gen_graphs(0)
        self.assertEqual(len(gs0), 1)
        self.assertTrue(dig() in gs0)
        
        gs1 = gen_graphs(1)        
        
        self.assertEqual(len(gs1), 2)    
        self.assertTrue(dig(1, []) in gs1)
        
    def test_assert_dig(self):
        
        self.assertDiGraphEqual(dig(), dig())
        
        with self.assertRaises(Exception):
            self.assertDiGraphEqual(dig(), dig('a',[]))        

    def test_dfs(self):

        with self.assertRaises(Exception):
            self.assertEquals(dig().dfs('a'), [])
                        
        self.assertEquals(dig('a',[]).dfs('a').verteces(), ['a'])
                        
        for g in GRAPHS_3:
            try:
                visit = g.dfs(1)
                self.assertLessEqual(visit.last_time(), 3*2)
                self.assertEqual(visit.log(1).finish_time, 
                                  visit.last_time())
            except Exception as e:
                self.raise_graph(e, g, visit)
          
    def test_bfs_empty(self):
        with self.assertRaises(Exception):
            dig().bfs('a')
        
    def test_bfs_not_found(self):
        with self.assertRaises(Exception):
            dig('a').bfs('b')

    def test_bfs_root_parent(self):
        
        visit = dig('a', ['a']).bfs('a')        
        self.assertEqual(visit.log('a').parent, None )

    def test_bfs_parent(self):
        
        visit = dig('a', ['a', 'b']).bfs('a')        
        self.assertEqual(visit.log('b').parent, 'a' )
              
             
    def test_bfs(self):

                                                        
        self.assertEquals(dig('a',[]).bfs('a').verteces(), ['a'])
                
        for g in GRAPHS_3:
            try:
                visit = g.bfs(1)
                self.assertSubset(set(visit.verteces()), g.verteces() )                
                self.assertLessEqual(visit.last_time(), 3)
            except Exception as e:                                                
                self.raise_graph(e, g, visit)
    

    def test_full_graph(self):
        self.assertDiGraphEqual(full_graph([]),
                                dig())
        self.assertDiGraphEqual(full_graph(['a']),
                                dig('a', ['a']))
        self.assertDiGraphEqual(full_graph(['a','b']), 
                                dig('a',['a','b'],
                                    'b',['a','b']))


    def test_dag(self):
        self.assertDiGraphEqual(dag([]), dig())
        self.assertDiGraphEqual(dag(['a']), dig('a', []))
        self.assertDiGraphEqual(dag(['a', 'b']), dig('a', ['b']))
        self.assertDiGraphEqual(dag(['a','b','c']),
                                dig('a',['b','c'],
                                    'b',['c']))

    def test_list_graph(self):
        with self.assertRaises(Exception):
            list_graph(-4)
                    
        self.assertEquals(dig(), list_graph(0))
        self.assertEquals(dig(1,[]), list_graph(1))
        self.assertEquals(dig(1,[2],2,[3]), list_graph(3))

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

