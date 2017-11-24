
class LinkedList:
    """
        LinkedList
        
        This class is similar to 'UnorderedList' in the book, with these differences:
            - has more pythonic names
            - tries to mimic more closely the behaviour of default Python list, raising exceptions on 
              boundary conditions like removing non exisiting elements.
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
        """ Returns True if the list has no nodes, True otherwise """
        raise Exception("TODO implement me!")


    def add(self,item):    
        """ Adds item at the beginning of the list """
        raise Exception("TODO implement me!")


    def size(self):
        """ Returns the size of the list """
        raise Exception("TODO implement me!")


    def search(self,item):
        """ Returns True if item is present in list, False otherwise        
        """
        raise Exception("TODO implement me!")
        
    def remove(self, item):
        """ Removes first occurrence of item from the list
        
            If item is not found, raises an Exception.
        """
        raise Exception("TODO implement me!")
    
    def append(self, e):
        """ Appends element e to the end of the list.
            
            For this exercise you can write the O(n) version
        """                
        
        raise Exception("TODO implement me!")
    
    def insert(self, i, e):
        """ Insert an item at a given position. 

            The first argument is the index of the element before which to insert, so list.insert(0, e)
            inserts at the front of the list, and list.insert(list.size(), e) is equivalent to list.append(e).
            When i > list.size(), raises an Exception (default Python list appends instead to the end :-/ )
            
        """        
        raise Exception("TODO implement me!")                
        
    def index(self, e):
        """ Return the index in the list of the first item whose value is x. 
            If there is no such item, an exception is raised. 
        """
        
        raise Exception("TODO implement me!")                        

        
    def pop(self):
        """ Remove the last item of the list, and return it. 
            
            If the list is empty, an exception is raised. 
        """
        raise Exception("TODO implement me!")        
