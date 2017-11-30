#
#      Library of utilities for Scientific Programming Algolab 
# 
#                   DO NOT MODIFY THIS FILE !
#

import unittest
import sys


def _get_generic_tree_def():
    """ Hack to get the damned GenericTree definition without excplicitly importing the module. 
    """

    if 'tree' in sys.modules: 
        return getattr(sys.modules['tree'], 'GenericTree')
    elif 'tree_solution' in sys.modules: 
        return getattr(sys.modules['tree_solution'], 'GenericTree')
    else:
        raise Exception("Cannot find a module containg GenericTree definition !")        


def gt(*args):
    """ Shorthand function that returns a GenericTree containing the provided 
        data and children. First parameter is the data, the following ones are the children.
        
        Usage examples:
        
        >>> print gt('a')
        a
        
        >>> print gt('a', gt('b'), gt('c'))            
            a
            ├b            
            └c
                            
    """
    if (len(args) == 0):
        raise Exception("You need to provide at least one argument for the data!")
        
    data = args[0]
    children = args[1:]
    
    GenericTree = _get_generic_tree_def()
    
    r = GenericTree(data)    
    for c in reversed(children):        
        c._sibling = r._child
        c._parent = r
        r._child = c        
    return r

def str_trees(t1, t2, error_row=-1):
    """ Returns a string version of the two trees side by side
    
        If error_row is given, the line in error is marked.
        If error_row == -1 it is ignored 
    """
    
    s1 = str(t1)
    s2 = str(t2)

    lines1 = s1.split("\n")
    lines2 = s2.split("\n")                

    max_len1 = 0                
    for line in lines1:                                    
        max_len1 = max(len(line.rstrip()), max_len1)        
        
    max_len2 = 0                
    for line in lines2:                                    
        max_len2 = max(len(line.rstrip()), max_len2)
    
    strings = []

    i = 0

    while i < len(lines1) or i < len(lines2):

        if i < len(lines1): 
            strings.append(lines1[i].rstrip())
            len1 = len(lines1[i].rstrip())
        else:
            len1 = 0
                       
        if (i < len(lines2)):
            len2 = len(lines2[i].rstrip())
            
            pad_len1 = 4 + max_len1 - len1
            strings.append((" " * pad_len1) + lines2[i].rstrip()) 
        else:
            len2 = 0
            
        if (error_row == i):
            pad_len2 = 2 + max_len1 + max_len2 - len1 - len2
            strings.append((" " * pad_len2) + "<--- DIFFERENT ! ")
            
        strings.append("\n")

        i += 1
    
    return "".join(strings)


class GenericTreeTest(unittest.TestCase):

    def assertRoot(self, t):
        """ Checks provided node t is a root, if not raises Exception """
                          
        self.assertTrue(t.is_root(), "Detached node " + t.data() + " is not a root, does it have still the _parent or _sibling set to something ?")

    
    def assertReturnNone(self, ret, function_name):
        """ Asserts method result ret equals None """
        self.assertEqual(None, ret, 
                          function_name 
                          + " specs say nothing about returning objects! Instead you are returning " + str(ret))
    
    
    def assertTreeEqual(self, t1, t2):
        """ Asserts the trees t1 and t2 are equal """
        
        GenericTree = _get_generic_tree_def()
        
        def rec_assert(c1, c2, row):                    
            
            if c1 == None:
                raise Exception("Found a None node in left tree! \n\n"
                                + str_trees(t1,t2,row))         
            if c2 == None:
                raise Exception("Found a None node in right tree !\n\n"
                                + str_trees(t1,t2,row))
            
            if c1.data() != c2.data():
                raise Exception("data() is different!\n\n" 
                                + str_trees(t1,t2,row))
            
            self.assertTrue(c1 == t1 or c1.parent() != None, 
                            "Left parent is None!"
                           + "\n\n" +  str_trees(t1,t2,row) )

            self.assertTrue(c2 == t2 or c2.parent() != None, 
                            "Right parent is None!" 
                             + "\n\n" +  str_trees(t1,t2,row) )            
            
            self.assertTrue(c1.parent() == None or isinstance(c1.parent(), GenericTree), 
                           "Left parent is not a GenericTree instance!"
                            + "\n\n" +  str_trees(t1,t2,row) )
            self.assertTrue(c2.parent() == None or isinstance(c2.parent(), GenericTree), 
                           "Right parent is not a GenericTree instance!"
                            + "\n\n" +  str_trees(t1,t2,row) )
            
            if (c1.parent() == None):
                if (c2.parent() != None):
                    raise Exception("Different parents! "
                                    + "Left parent = None   Right parent.data() = " + str(c2.parent().data()) 
                                    + "\n\n" + str_trees(t1,t2,row) )
                                    
            else:    
                if (c2.parent() == None):                    
                    raise Exception("Different parents! "
                                    + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent = None"
                                    + "\n\n" + str_trees(t1,t2,row)) 
                else: # let's just check data for now
                    self.assertEquals(c1.parent().data(), c2.parent().data(),
                                  "Different parents ! " 
                                 + "Left parent.data() = " + str(c1.parent().data()) 
                                    + "   Right parent.data() = " + str(c2.parent().data()
                                    + "\n\n" + str_trees(t1,t2,row) ))
            i = 0            
            
            cs1 = c1.children()
            cs2 = c2.children()
            if (len(cs1) != len(cs2)):
                raise Exception("Children sizes are different !\n\n"
                                + str_trees(t1, t2, row + min(len(cs1), len(cs2))) )
            while (i < len(cs1) ):
                rec_assert(cs1[i], cs2[i], row + 1)   
                i += 1 
        
        rec_assert(t1, t2, 0)

        
        
        
class TreeTestTest(GenericTreeTest):    
    """ Tests the test itself ... """

    
    def test_str_trees(self):
        self.assertTrue('a' in str_trees(gt('a'), gt('b')))
        self.assertTrue('b' in str_trees(gt('a'), gt('b')))
        
        self.assertTrue('a' in str_trees(gt('a', gt('b')), gt('b', gt('c'))))
        self.assertTrue('c' in str_trees(gt('a', gt('b')), gt('b', gt('c'))))
    
    def test_assert_tree_equal(self):
        self.assertTreeEqual(gt('a'), gt('a'))
        self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b')))
        
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a'), gt('b'))            
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('c')))
        
        # different structure
        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b')), gt('a', gt('b',gt('c'))))

        with self.assertRaises(Exception):
            self.assertTreeEqual(gt('a', gt('b',gt('c'))), gt('a', gt('b')))        
    
    def test_print(self):
        # self.assertTreeEqual(gt('a', gt('b', gt('v')), gt('b', gt('v'))), gt('a', gt('b', gt('v'), gt('b', gt('v'))), gt('b')))
        return None 
        