import unittest
import CLP_sorter

class Test_CLP_sorter(unittest.TestCase):

    #integers normal sorting
    def test_sort_integer(self):
        list = ['1', '2', '3']
        expected = ['1', '2', '3'] 
        result = CLP_sorter.sort_lines(list)
        self.assertEqual(result, expected)
    
    #integers reverse sorting    
    def test_sort_integer_reverse(self):
        list = ['1', '2', '3']
        expected = ['3', '2', '1']  
        result = CLP_sorter.sort_lines(list, reverse=True)
        self.assertEqual(result, expected)

    #strings normal sorting(132)
    def test_sort_string(self):
        list = ['one', 'two', 'three']
        expected = ['one', 'three', 'two']  
        result = CLP_sorter.sort_lines(list)
        self.assertEqual(result, expected)
        
    #strings reverse sorting (231)
    def test_sort_string_reverse(self):
        list = ['one', 'two', 'three']
        expected = ['two', 'three', 'one']  
        result = CLP_sorter.sort_lines(list, reverse=True)
        self.assertEqual(result, expected)

    #floats normal sorting
    def test_sort_float(self):
        list = ['1.5', '2.5', '3.5']
        expected = ['1.5', '2.5', '3.5']  
        result = CLP_sorter.sort_lines(list)
        self.assertEqual(result, expected)
    
    #floats reverse sorting
    def test_sort_float_reverse(self):
        list = ['1.5', '2.5', '3.5']
        expected = ['3.5', '2.5', '1.5']
        result = CLP_sorter.sort_lines(list, reverse=True)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
