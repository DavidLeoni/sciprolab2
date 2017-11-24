from linked_list import *
import unittest

        
class LinkedListTest(unittest.TestCase):
    """ Test cases for LinkedList v2
    
        Test cases are improved by adding a new method myAssert(self, unordered_list, python_list)         
    """    
    
    def myAssert(self, unordered_list, python_list):
        """ Checks provided unordered_list can be represented as the given python_list. Since v2
        """
        self.assertEqual(unordered_list.to_python(), python_list)
        # we check this new invariant about the size
        self.assertEqual(unordered_list.size(), len(python_list)) 
        # we check this new invariant about the last element
        if len(python_list) != 0:
            self.assertEqual(unordered_list.last(), python_list[-1]) 
    
class AddTest(LinkedListTest):
    
    def test_init(self):
        ul = LinkedList()
    
    def test_str(self):
        ul = LinkedList()
        self.assertTrue('LinkedList' in str(ul))
        ul.add('z')
        self.assertTrue('z' in str(ul))
        ul.add('w')
        self.assertTrue('z' in str(ul))
        self.assertTrue('w' in str(ul))            
            
    def test_is_empty(self):
        ul = LinkedList()
        self.assertTrue(ul.is_empty())        
        ul.add('a')
        self.assertFalse(ul.is_empty())        
        
    def test_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = LinkedList()
        self.myAssert(ul, [])
        ul.add('b')
        self.myAssert(ul, ['b'])
        ul.add('a')
        self.myAssert(ul, ['a', 'b'])

class SizeTest(LinkedListTest):        
    def test_size(self):
        ul = LinkedList()
        self.assertEqual(ul.size(), 0)
        ul.add("a")
        self.assertEqual(ul.size(), 1)
        ul.add("b")
        self.assertEqual(ul.size(), 2)

class SearchTest(LinkedListTest):         
    def test_search(self):
        ul = LinkedList()
        self.assertFalse(ul.search("a"))        
        ul.add("a")
        self.assertTrue(ul.search("a"))
        self.assertFalse(ul.search("b"))
        ul.add("b")
        self.assertTrue(ul.search("a"))
        self.assertTrue(ul.search("b"))       
        
class RemoveTest(LinkedListTest):   
    
    def test_remove_empty_list(self):
        ul = LinkedList()
        with self.assertRaises(Exception):
            ul.remove('a')
        
    def test_remove_one_element(self):
        ul = LinkedList()
        ul.add('a')
        with self.assertRaises(Exception):
            ul.remove('b')
        ul.remove('a')
        self.assertEqual(ul.to_python(), [])
        
    def test_remove_two_element(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        with self.assertRaises(Exception):
            ul.remove('c')
        ul.remove('b')
        self.assertEqual(ul.to_python(), ['a'])        
        ul.remove('a')
        self.assertEqual(ul.to_python(), [])        

        
    def test_remove_first_occurrence(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('b')
        with self.assertRaises(Exception):
            ul.remove('c')
        ul.remove('b')
        self.assertEqual(ul.to_python(), ['b'])        
        ul.remove('b')
        self.assertEqual(ul.to_python(), [])

class AppendTest(LinkedListTest):           
        
    def test_append(self):
        ul = LinkedList()
        ul.append('a')        
        self.myAssert(ul,['a'])
        ul.append('b')                
        self.myAssert(ul,['a', 'b'])
        
        
class InsertTest(LinkedListTest):
    
    def test_insert_empty_list_zero(self):
        ul = LinkedList()
        ul.insert(0, 'a')        
        self.myAssert(ul, ['a'])

    def test_insert_empty_list_out_of_bounds(self):
        ul = LinkedList()        
        with self.assertRaises(Exception):
            ul.insert(1, 'a')
        with self.assertRaises(Exception):
            ul.insert(-1, 'a')

    def test_insert_one_element_list_before(self):
        ul = LinkedList()                
        ul.add('b')
        ul.insert(0, 'a')
        self.myAssert(ul, ['a','b'])

        
    def test_insert_one_element_list_after(self):
        ul = LinkedList()                
        ul.add('a')
        ul.insert(1, 'b')
        self.myAssert(ul, ['a','b'])                    

    def test_insert_two_element_list_insert_before(self):
        ul = LinkedList()                
        ul.add('c')
        ul.add('b')
        ul.insert(0, 'a')
        self.myAssert(ul, ['a','b','c'])
        
    def test_insert_two_element_list_insert_middle(self):
        ul = LinkedList()                
        ul.add('c')
        ul.add('a')
        ul.insert(1, 'b')
        self.myAssert(ul, ['a','b', 'c'])

    def test_insert_two_element_list_insert_after(self):
        ul = LinkedList()                
        ul.add('b')
        ul.add('a')
        ul.insert(2, 'c')
        self.myAssert(ul, ['a','b', 'c'])
        
class IndexTest(LinkedListTest): 
    
    def test_index_empty_list(self):
        ul = LinkedList()
        with self.assertRaises(Exception):
            ul.index('a')        
    
    def test_index(self):
        ul = LinkedList()
        ul.add('b')        
        self.assertEqual(ul.index('b'),  0)
        with self.assertRaises(Exception):
            ul.index('a')
        ul.add('a')        
        self.assertEqual(ul.index('a'),  0)
        self.assertEqual(ul.index('b'),  1)
              
            
class PopTest(LinkedListTest):
    
    def test_pop_empty(self):
        ul = LinkedList()
        with self.assertRaises(Exception):
            ul.pop()

    def test_pop_one(self):
        ul = LinkedList()
        ul.add('a')
        x = ul.pop()
        self.assertEqual('a', x)
        
    def test_pop_two(self):
        ul = LinkedList()
        ul.add('b')
        ul.add('a')
        x = ul.pop()
        self.assertEqual('b', x)
        self.myAssert(ul, ['a'])
        y = ul.pop()
        self.assertEqual('a', y)
        self.myAssert(ul, [])
        
    def test_last(self):
        """ This tests only simple cases. More in-depth testing will be provided by calls to myAssert """
        
        ul = LinkedList()
        with self.assertRaises(Exception):
            ul.last()        
        ul.add('b')
        self.assertEqual(ul.last(), 'b')
        ul.add('a')
        self.assertEqual(ul.last(), 'b')