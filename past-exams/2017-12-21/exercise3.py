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

    def spantree(self, source):
        
        """ Returns a dictionary where the keys are verteces, and each vertex v is associated
            to the shortest path to go from the root to reach v, represented as a tuple of labels
            which includes the node itself. 

            - If node is unreachable, the path will be the empty tuple.
            - Source has empty path
            - Verteces immediately connected to source have only source in the associated tuple.
            - if source is not a vertex, raises an Exception

            HINT: to implement this, copy and edit either dfs or bfs. Question: which one ?
                         
        """
        
        raise Exception("TODO IMPLEMENT ME !")