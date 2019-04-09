import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # tests if list = None raises ValueError
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        # tests max for sorted list
        num_list = [1, 2, 3]
        self.assertEqual(max_list_iter(num_list), 3)
        # tests max for list with negatives
        num_list2 = [-1, 0, -4]
        self.assertEqual(max_list_iter(num_list2), 0)
        # tests max for empty list
        num_list3 = []
        self.assertEqual(max_list_iter(num_list3), None)

    def test_reverse_rec(self):
        # tests for sorted list
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        # tests for list with repeats and negative nums
        self.assertEqual(reverse_rec([-1,0,0]),[0,0,-1])
        # tests for list with all same numbers
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        # used to check for exception list = None
        with self.assertRaises(ValueError):
            reverse_rec(None)
        # tests for list with decimals
        self.assertEqual(reverse_rec([1.2,3.5,2.1]),[2.1,3.5,1.2])
        # tests for empty list
        self.assertEqual(reverse_rec([]),[])
        # tests for list length 1
        self.assertEqual(reverse_rec([1]), [1])

    def test_bin_search(self):
        # tests for target in middle of list
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)
        # tests for target as first number in the list
        list_val2 = [0,1,2,3,4,7,8,9,10] 
        low = 2
        high = 8
        self.assertEqual(bin_search(1, low, high, list_val2), None)
        # test for target not in range
        list_val3 = [1,2,3,4,7]
        low = 0
        high = 4
        self.assertEqual(bin_search(7, 0, 4, list_val3), 4 )
        # used to check for exception list = None
        list_val4 = None
        with self.assertRaises(ValueError):
           bin_search(1, 0, 4, list_val4)
        # tests for when list has length 1
        list_val5 = [1]
        self.assertEqual(bin_search(1, 0, 1, list_val5), 0)
        # test for target to the left of midpoint
        list_val6 = [1,2,3,4]
        self.assertEqual(bin_search(2, 0, 3, list_val6), 1)
        # test for target to the right of midpoint
        list_val7 = [1,2,3,4]
        self.assertEqual(bin_search(3, 0, 3, list_val7), 2)
        # test target not in list
        list_val7 = [1,2,3,4]
        self.assertEqual(bin_search(7, 0, 3, list_val7), None)
        # test for list with negative numbers
        list_val8 = [-2,-1,0,1,2]
        self.assertEqual(bin_search(1, 0, 3, list_val8), 3)
        # test for target as last number in list
        list_val9 = [1,2,3]
        self.assertEqual(bin_search(3, 0, 2, list_val9), 2)

if __name__ == "__main__":
        unittest.main()

    
