from exercise2 import *
import unittest


class LinkedListTest(unittest.TestCase):

    def myAssert(self, linked_list, python_list):
        """ Checks provided linked_list can be represented as the given python_list.
        """
        self.assertEqual(linked_list.to_python(), python_list)
        # check this new invariant about the size        
        self.assertEqual(linked_list.size(), len(python_list)) 
    

class AddTest(LinkedListTest):
    
    def test_01_init(self):
        ul = LinkedList()
    
    def test_02_str(self):
        ul = LinkedList()
        self.assertTrue('LinkedList' in str(ul))
        ul.add('z')
        self.assertTrue('z' in str(ul))
        ul.add('w')
        self.assertTrue('z' in str(ul))
        self.assertTrue('w' in str(ul))
                
    def test_03_is_empty(self):
        ul = LinkedList()
        self.assertTrue(ul.is_empty())        
        ul.add('a')
        self.assertFalse(ul.is_empty())        
        
    def test_04_add(self):
        """ Remember 'add' adds stuff at the beginning of the list ! """
        
        ul = LinkedList()
        self.assertEqual(ul.to_python(), [])
        ul.add('b')
        self.assertEqual(ul.to_python(), ['b'])
        ul.add('a')
        self.assertEqual(ul.to_python(), ['a', 'b'])
               
class EqTest(LinkedListTest):

    def test_01_empty(self):
        list1 = LinkedList()
        list2 = LinkedList()
        self.assertEqual(list1, list2)

    def test_02_one_same(self):
        list1 = LinkedList()
        list1.add('a')
        list2 = LinkedList()
        list2.add('a')
        self.assertEqual(list1, list2)

    def test_03_one_diff(self):
        list1 = LinkedList()
        list1.add('a')
        list2 = LinkedList()
        list2.add('b')
        self.assertNotEqual(list1, list2)

    def test_04_one_two(self):
        list1 = LinkedList()
        list1.add('a')
        list2 = LinkedList()
        list2.add('b')
        list2.add('a')
        self.assertNotEqual(list1, list2)

    def test_05_two_one(self):
        list1 = LinkedList()
        list1.add('b')
        list1.add('a')
        list2 = LinkedList()
        list2.add('a')
        self.assertNotEqual(list1, list2)

        
    def test_06_two_eq(self):
        list1 = LinkedList()
        list1.add('b')
        list1.add('a')
        list2 = LinkedList()
        list2.add('b')
        list2.add('a')
        self.assertEqual(list1, list2)
        
    def test_07_two_not_eq(self):
        list1 = LinkedList()
        list1.add('b')
        list1.add('a')
        list2 = LinkedList()
        list2.add('c')
        list2.add('a')
        self.assertNotEqual(list1, list2)
        
    def test_08_three_rep_eq(self):
        list1 = LinkedList()
        list1.add('a')
        list1.add('b')
        list1.add('a')
        list2 = LinkedList()
        list2.add('a')
        list2.add('b')
        list2.add('a')
        self.assertEqual(list1, list2)

    def test_09_three_rep_diff(self):
        list1 = LinkedList()
        list1.add('a')
        list1.add('c')
        list1.add('a')
        list2 = LinkedList()
        list2.add('a')
        list2.add('b')
        list2.add('a')
        self.assertNotEqual(list1, list2)

class RemsubTest(LinkedListTest):
    
    def test_01_empty(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), [])

    def test_02_one_same(self):
        list1 = LinkedList()
        list1.add('a')
        list2 = LinkedList()
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), [])

    def test_03_one_diff(self):
        list1 = LinkedList()
        list1.add('a')
        list2 = LinkedList()
        list2.add('b')
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), ['a'])
        
    def test_04_two_one_match(self):
        list1 = LinkedList()
        list1.add('a')
        list1.add('a')
        list2 = LinkedList()
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), ['a'])
        
    def test_05_two_two_match(self):
        list1 = LinkedList()
        list1.add('a')
        list1.add('a')
        list2 = LinkedList()
        list2.add('a')
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), [])
        
    def test_06_three_borders(self):
        list1 = LinkedList()
        list1.add('c')
        list1.add('b')
        list1.add('a')
        list2 = LinkedList()
        list2.add('c')
        list2.add('a')
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), ['b'])

    def test_07_three_middle(self):
        list1 = LinkedList()
        list1.add('c')
        list1.add('b')
        list1.add('a')        
        list2 = LinkedList()
        list2.add('b')
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), ['a', 'c'])
        
    def test_08_three_end(self):
        list1 = LinkedList()
        list1.add('b')
        list1.add('b')
        list1.add('a')        
        list2 = LinkedList()
        list2.add('b')
        list2.add('b')
        list1.remsub(list2)
        self.assertEqual(list1.to_python(), ['a'])
        
        