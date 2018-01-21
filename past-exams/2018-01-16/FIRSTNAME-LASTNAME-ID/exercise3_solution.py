class GenericTree:
    """ This is a stripped down version of GenericTree we saw in class.
    
        A tree in which each node can have any number of children. 
    
        Each node is linked to its parent and to its immediate sibling on the right
    """
    
    def __init__(self, data):
        self._data = data
        self._child = None
        self._sibling = None
        self._parent = None        

    def data(self):
        return self._data    
    
    def child(self):
        return self._child    
    
    def sibling(self):
        return self._sibling
    
    def parent(self):
        return self._parent
        
    def is_root(self):
        """ Return True if the node is a root of a tree, False otherwise
        
            A node is a root whenever it has no parent nor siblings.
        """
        return self._parent == None and self._sibling == None
    
    def is_subtree(self):
        """ Returns True if the node is a subtree of another tree
        
            A subtree always has a parent 
        """
        return self._parent != None
        
        
        
    def __str__(self):
        """ Returns a pretty string of the tree """
        
        def str_branches(node, branches):
            """ Returns a string with the tree pretty printed. 

                branches: a list of characters representing the parent branches. Characters can be either ` ` or '│'            
            """
            strings = [str(node._data)]
            current = node._child
            while (current != None):
                if current._sibling == None:            
                    joint = '└'  
                else:
                    joint = '├'


                strings.append('\n')
                for b in branches:
                     strings.append(b)
                strings.append(joint)
                if current._sibling == None:            
                    branches.append(' ')
                else:
                    branches.append('│')                        
                strings.append(str_branches(current, branches))
                branches.pop()
                current = current._sibling

            return "".join(strings)
        
        return str_branches(self, [])
                
    def has_child(self):
        """ Returns True if this node has a child, False otherwise """

        return self._child != None
    
    def insert_child(self, new_child):        
        """ Inserts new_child at the beginning of the children sequence. """
        
        new_child._sibling = self._child
        new_child._parent = self
        self._child = new_child


    def detach_child(self):
        """ Detaches the first child. 
        
            if there is no child, raises an Exception 
        """

        if (self._child == None):
            raise Exception("There is no child !")            
        else:
                        
            detached = self._child
            self._child = self._child._sibling 
            detached._parent = None
            detached._sibling = None                                

    def detach_sibling(self):
        """ Detaches the first sibling.
        
            If there is no sibling, raises an Exception 
        """
        
        if (self._sibling == None):
            raise Exception("There is no sibling !")
        else:
            detached = self._sibling            
            self._sibling = self._sibling._sibling             
            detached._parent = None
            detached._sibling = None

    def count_leaves(self):
        """  Return the number of leaves in the tree (= nodes with no children at the bottom)

            - Root node can never be considered a leaf        
            - Must execute in O(n) where n is the number of nodes of the tree.
            - It is acceptable for this method to be implemented in a recursive way.
        """
        current = self._child
        
        count = 0        
        while current != None:            
            if current._child == None:
                count += 1
                current = current._sibling
            else:
                count += current.count_leaves()
                current = current._sibling
        return count

    def detach_leaves(self):
        """ Detaches all the leaves from the tree (= nodes with no children at the bottom)
        
            - Root node can never be considered a leaf
            - Must execute in O(n) where n is the number of nodes of the tree.
            - In order to solve it, feel free to use the provided detach_child and detach_sibling methods
            - It is acceptable for this method to be implemented in a recursive way.
            
        """
        current = self._child
        prev = None
        while current != None:
            if current._child == None:
                # notice we must change current before detaching, otherwise we lose the sibling
                current = current._sibling
                if prev == None:
                    self.detach_child()
                else:
                    prev.detach_sibling()
            else:
                current.detach_leaves()
                prev = current
                current = current._sibling

