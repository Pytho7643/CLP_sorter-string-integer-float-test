import unittest
import CLP_sorter

class Test_CLP_sorter(unittest.TestCase):

  def test_sort(self):
    list = ['1', '2', '3']
    expected = ['3', '2', '1']

    result = CLP_sorter.sort_lines(list, reverse=True)
    self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()