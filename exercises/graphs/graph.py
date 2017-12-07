import pprint
from queue import Queue
from algolab import dig, DiGraphTest

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
            ret = list(self._logs.values())
        else:
            
            ret = list(filter(lambda log: log.discovery_time > -1, self._logs.values())) 
        ret.sort(key=sort_by, reverse=descendant)
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
        return list(map(lambda vertex_log:vertex_log.vertex,                                      
                   self.logs(sort_by=sort_by, 
                             descendant=descendant,
                             get_all=get_all)))

    
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
    
    def remove_vertex(self, vertex):
        """ Removes the provided vertex  and returns it
            
            If the vertex is not found, raises an Exception.
        """
                
        if not vertex in self._edges:
            raise Exception("Couldn't find vertex:" +str(vertex))
        
        for source in self.verteces():
            if vertex in self._edges[source]:
                self._edges[source].remove(vertex)
        
        return self._edges.pop(vertex)
        
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
        
        sorted_verteces = sorted(self._edges.keys(), key=str)
        
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



    def adj(self, vertex):
        """ Returns the verteces adjacent to vertex. 
            
            NOTE: verteces are returned in a NEW list.
            Modifying the list will have NO effect on the graph!
        """
        if not vertex in self._edges:
            raise Exception("Couldn't find a vertex " + str(vertex))
        
        return self._edges[vertex][:]
      
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
         
    def is_empty(self):
        """  A DiGraph for us is empty if it has no verteces and no edges """
        
        return len(self._edges) == 0

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
        raise Exception("TODO IMPLEMENT ME !")                                
    
    def reverse(self):
        """ Reverses the direction of all the edges 
        
            Note this one changes in-place the graph: does **not** create a new instance
            and does *not* return anything !!        
        """
        raise Exception("TODO IMPLEMENT ME !")                                
    
    def has_self_loops(self):
        """ Returns True if the graph has any self loop (a.k.a. cap), False otherwise """
        
        raise Exception("TODO IMPLEMENT ME !")                                
        
    def remove_self_loops(self):
        """ Removes all of the self-loops edges (a.k.a. caps) 
            
            NOTE: Removes just the edges, not the verteces!
        """

        raise Exception("TODO IMPLEMENT ME !")                                
                
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
       
        raise Exception("TODO IMPLEMENT ME !")                                
        


def full_graph(verteces):
    """ Returns a DiGraph which is a full graph with provided verteces list.
    
        In a full graph all verteces link to all other verteces (including themselves!).
    """
    
    raise Exception("TODO IMPLEMENT ME !")                                

def dag(verteces):
    """ Returns a DiGraph which is DAG (Directed Acyclic Graph) made out of provided verteces list
    
        Provided list is intended to be in topological order.
        NOTE: a DAG is ACYCLIC, so caps (self-loops) are not allowed !!
    """

    raise Exception("TODO IMPLEMENT ME !")                                
    
def list_graph(n):
    """ Return a graph of n verteces displaced like a 
        monodirectional list:  1 -> 2 -> 3 -> ... -> n 
        
        Each vertex is a number i, 1 <= i <= n  and has only one edge connecting it
        to the following one in the sequence        
        If n = 0, return the empty graph.
        if n < 0, raises an Exception.
    """    
        
    raise Exception("TODO IMPLEMENT ME !")                                
    
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
    
    raise Exception("TODO IMPLEMENT ME !")                                
    

def odd_line(n):
    """ Returns a DiGraph with n verteces, displaced like a line of odd numbers
    
        Each vertex is an odd number i, for  1 <= i < 2n. For example, for
        n=4 verteces are displaced like this:
                
        1 -> 3 -> 5 -> 7
        
        For n = 0, return the empty graph
            
    """
        
    raise Exception("TODO IMPLEMENT ME !")
    
def even_line(n):
    """ Returns a DiGraph with n verteces, displaced like a line of even numbers
    
        Each vertex is an even number i, for  2 <= i <= 2n. For example, for
        n=4 verteces are displaced like this:
                
        2 <- 4 <- 6 <- 8
        
        For n = 0, return the empty graph
            
    """
        
    raise Exception("TODO IMPLEMENT ME !")
    
def quads(n):
    """ Returns a DiGraph with 2n verteces, displaced like a strip of quads.
    
        Each vertex is a number i,  1 <= i <= 2n. 
        For example, for n = 4, verteces are displaced like this:
                
        1 -> 3 -> 5 -> 7
        ^    |    ^    |
        |    ;    |    ;
        2 <- 4 <- 6 <- 8
        
        where 
        
          ^                                         |
          |  represents an upward arrow,   while    ;  represents a downward arrow        
    
    """

    raise Exception("TODO IMPLEMENT ME !")

def pie(n):
    """ Returns a DiGraph with n+1 verteces, displaced like a polygon with a perimeter 
        of n verteces progressively numbered from 1 to n. A central vertex numbered zero 
        has outgoing edges to all other verteces.
        
        For n = 0, return the empty graph.
        For n = 1, return vertex zero connected to node 1, and node 1 has a self-loop.
        
    """
        
    raise Exception("TODO IMPLEMENT ME !")
    
def flux(depth):
    """ Returns a DiGraph with 1 + (d * 3) verteces displaced like a Y:
        - from a central node numbered 0, three branches depart  
        - all edges are directed outward
        - on each branch there are 'depth' verteces. 
        - if depth < 0, raises a ValueError
                
        For example, for depth=2 we get the following graph (suppose arrows point outward):
        
             4         5
              \       /
               1     2
                \   /
                  0
                  |
                  3
                  |
                  6
        
    """
    raise Exception("TODO IMPLEMENT ME !")
