
class CircularQueue:
    """ A circular queue with a fixed capacity.
    """
    
    
    def __init__(self, capacity):
        """ Initializes the queue, reserving space for a number of elements equal to provided capacity.
        
            - If capacity is not an int, raises ValueError.
            - If capacity is <= 0, raises ValueError.
            - Complexity: O(capacity)
        """                
        
        raise Exception("TODO IMPLEMENT ME")
        
    def __str__(self):
        """ For potentially complex data structures like this one, having a __str__ method is essential to 
            quickly inspect the data by printing it. 
        """        
        
        return "CircularQueue: " + str(vars(self))

        
        
    def size(self):
        """ Return the size of the queue.
        
            - Complexity: O(1)
        """

        raise Exception("TODO IMPLEMENT ME")
    
    def capacity(self):
        """ Return the capacity of the queue, that is, the maximum number of allowed elements in the queue.
            
            - Complexity: O(1)
        """
        raise Exception("TODO IMPLEMENT ME")

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise.
        
            - Complexity: O(1)
        """
        raise Exception("TODO IMPLEMENT ME")
        
    
    def top(self):
        """ Return the element at the head of the queue, without removing it. 
        
            - If the queue is empty, raises LookupError.            
            - Complexity: O(1)
        """
        raise Exception("TODO IMPLEMENT ME")

            
    def enqueue(self, v):
        """ Enqueues provided element v at the end of the queue.
        
            - If the queue is full, raises BufferError.
            - Complexity: O(1)
        """
        
        raise Exception("TODO IMPLEMENT ME")
        
    def dequeue(self):
        """ Removes head element and returns it.
            
            - If the queue is empty, raises a LookupError.
            - Complexity: O(1)
        """
        
        raise Exception("TODO IMPLEMENT ME")
    
