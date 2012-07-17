import random
import unittest
import src.sort.recursion_insertion_sort as sort

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.in_array = random.sample(range(0, 100), 20)
        self.expected_array = sorted(self.in_array)

    def test_sort(self):
        result_array  = sort.recursion_insertion_sort( self.in_array)  
    
        self.assertEqual(self.expected_array, result_array )

