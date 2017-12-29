class Node:
    """ A Node of an LinkedList. Holds data provided by the user. """
    
    def __init__(self,initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,newdata):
        self._data = newdata

    def set_next(self,newnext):
        self._next = newnext


class LinkedList:
    """
        LinkedList - this is a stripped down verison of the LinkedList as seen in class
        
    """
        
    def __init__(self):
        self._head = None

    def to_python(self):
        """ Returns this LinkedList as a regular Python list. This method is very handy for testing.
        """
        python_list = []
        current = self._head        
        
        while (current != None):
            python_list.append(current.get_data())
            current = current.get_next()                       
        return python_list        
        
    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to 
            quickly inspect the data by printing it. 
        """
        current = self._head
        strings = []
        
        while (current != None):
            strings.append(str(current.get_data()))            
            current = current.get_next()            
        
        return "LinkedList: " + ",".join(strings)
        
        
    def is_empty(self):
        return self._head == None

    def add(self,item):    
        """ Adds item at the beginning of the list """
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

    def __eq__(self, other):
        """ Returns True if self is equal to other, that is, if all the data elements in the respective
            nodes are the same. Otherwise, return False.
            
            NOTE: compares the *data* in the nodes, NOT the nodes themselves !
        """
        
        raise Exception("TODO IMPLEMENT ME !")
        
        
    def remsub(self, rem):
        """ Removes the first elements found in this LinkedList that match subsequence rem
            rem: the subsequence to eliminate, which is also a LinkedList.
            
            Examples:
                aabca  remsub ac  =  aba 
                aabca  remsub cxa =  aaba  # when we find a never matching character in rem like 'x', 
                                             the rest of rem after 'x' is not considered.
                aabca  remsub ba  =  aac
                aabca  remsub a   =  abca
                abcbab remsub bb  =  acab
        """
        raise Exception("TODO IMPLEMENT ME !")
        
        
