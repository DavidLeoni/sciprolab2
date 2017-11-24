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
        LinkedList v1
        
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
        return self._head == None

    def add(self,item):    
        """ Adds item at the beginning of the list """
        new_head = Node(item)
        new_head.set_next(self._head)
        self._head = new_head

    def size(self):
        """ Returns the size of the list """
        current = self._head
        count = 0
        
        while (current != None):
            current = current.get_next()
            count += 1
            
        return count

    def search(self,item):
        """ Returns True if item is present in list, False otherwise        
        """
        current = self._head
        
        while (current != None):            
            if (current.get_data() == item):
                return True
            else:
                current = current.get_next()  
            
        return False
        
    def remove(self, item):
        """ Removes first occurrence of item from the list
        
            If item is not found, raises an Exception.
        """
        current = self._head        
        prev = None
        
        while (current != None):
            if (current.get_data() == item):
                if prev == None:  # we need to remove the head 
                    self._head = current.get_next()
                else:  
                    prev.set_next(current.get_next())
                    current = current.get_next()                    
                return  # Found, exits the function
            else:
                prev = current
                current = current.get_next() 
        
        raise Exception("Tried to remove a non existing item! Item was: " + str(item))
    
    def append(self, e):
        """ Appends element e to the end of the list.
            
            For this exercise you can write the O(n) version
        """                
        
        if self._head == None:
            self.add(e)
        else:                        
            current = self._head
            while (current.get_next() != None):
                current = current.get_next()
            current.set_next(Node(e))
    
    def insert(self, i, e):
        """ Insert an item at a given position. 

            The first argument is the index of the element before which to insert, so list.insert(0, e)
            inserts at the front of the list, and list.insert(list.size(), e) is equivalent to list.append(e).
            When i > list.size(), raises an Exception (default Python list appends instead to the end :-/ )
            
        """        
        if (i < 0):
            raise Exception("Tried to insert at a negative index! Index was:" + str(i))
            
        count = 0
        current = self._head
        prev = None
        
        while (count < i and current != None):
            prev = current
            current = current.get_next()
            count += 1
        
        if (current == None):
            if (count == i):
                self.append(e)
            else:
                raise Exception("Tried to insert outside the list ! "
                                + "List size=" + str(count) + "  insert position=" + str(i))
        else:
            #0 1
            #  i
            if (prev == None):
                self.add(e)
            else:
                new_node = Node(e)
                prev.set_next(new_node)
                new_node.set_next(current)                
        
    def index(self, e):
        """ Return the index in the list of the first item whose value is x. 
        
            If item is not found, raises an Exception.
        """
        
        current = self._head
        count = 0        
        
        while (current != None):
            if (current.get_data() == e):
                return count
            else:
                current = current.get_next()  
                count += 1
        
        raise Exception("Couldn't find element " + str(e) )
        

        
    def pop(self):
        """ Remove the last item of the list, and return it. 
            
            If the list is empty, an exception is raised. 
        """
        if (self._head == None):
            raise Exception("Tried to pop an empty list!")
        else:               
            
            current = self._head
             
            if (current.get_next() == None): # one element list
                last_item = self._head.get_data()
                self._head = None
            else:    # we have more than one element
                prev = None            
                while current.get_next() != None:  # current will reach last element
                    prev = current
                    current = current.get_next()                                                                                            
                last_item = current.get_data()
                prev.set_next(None)                              
                
            return last_item