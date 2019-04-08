import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        num_list = [1, 2, 3]
        self.assertEqual(max_list_iter(num_list), 3)
        num_list2 = [-1, 0, -4]
        self.assertEqual(max_list_iter(num_list2), 0)
        num_list3 = []
        self.assertEqual(max_list_iter(num_list3), None)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([-1,0,0]),[0,0,-1])
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)
        self.assertEqual(reverse_rec([1.2,3.5,2.1]),[2.1,3.5,1.2])
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )
        list_val2 = [0,1,2,3,4,7,8,9,10] 
        low = 2
        high = 8
        self.assertEqual(bin_search(1, low, high, list_val2), None )
        list_val3 = [1,2,3,4,7]
        low = 0
        high = 4
        self.assertEqual(bin_search(7, 0, 4, list_val3), 4 )      
        list_val4 = None
        with self.assertRaises(ValueError):  # used to check for exception
           bin_search(1, 0, 4, list_val4)
        list_val5 = [1]
        self.assertEqual(bin_search(1, 0, 1, list_val5), 0 )
        list_val6 = [1,2,3,4]
        self.assertEqual(bin_search(2, 0, 3, list_val6), 1 ) 
        list_val7 = [1,2,3,4]
        self.assertEqual(bin_search(3, 0, 3, list_val7), 2 )
        list_val7 = [1,2,3,4]
        self.assertEqual(bin_search(7, 0, 3, list_val7), None )
 
if __name__ == "__main__":
        unittest.main()

    
