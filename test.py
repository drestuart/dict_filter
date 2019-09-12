import unittest
from dict_filter.filter import dict_filter, FilterStructureError

# List of test cases:
#
# - None returns any value x
# - Empty list returns any list x 
# - List of ints returns indexed values in list x
#   - Index error cases x
#   - List value error cases x
# - Empty tuple returns any tuple x
# - Tuple of ints returns indexed values in tuple x
#   - Index error cases x
#   - Tuple value error cases x
# - Empty dictionary returns any dictionary
# - Non-empty dictionary causes recursion into dict value
# - Filter value is a function => Runs function on value
#   - Lambda function
#   - Named function
#   - Built-in function



class TestFilter(unittest.TestCase):

    simple_dict = {
        'a': 1,
        'b': (2, 4, 8, 16),
        'c': [3, 4, 5]
    }

    def test_none(self):
        """
        Test that None returns any value
        """

        result = dict_filter(self.simple_dict, {
            'a': None
        })

        self.assertEqual(result, {'a': 1})


    def test_empty_list(self):
        """
        Test that an empty list returns any list
        """

        result = dict_filter(self.simple_dict, {
            'c': []
        })

        self.assertEqual(result, {'c': [3, 4, 5]})


    def test_list_indices(self):
        """
        Test that a list of ints returns indexed values in list
        """

        result = dict_filter(self.simple_dict, {
            'c': [1, 0, -1, 2, -2]
        })

        self.assertEqual(result, {'c': [4, 3, 5, 5, 4]})


    def test_list_indices_index_error(self):
        """
        Test that filtering for indices out of range raises an index error
        """

        with self.assertRaises(IndexError):

            result = dict_filter(self.simple_dict, {
                'c': [5]
            })


    def test_list_indices_structure_error(self):
        """
        Test that filtering for indices out of range raises an index error
        """

        with self.assertRaises(FilterStructureError):

            result = dict_filter(self.simple_dict, {
                'c': ['wrong']
            })


    def test_empty_tuple(self):
        """
        Test that an empty tuple returns any tuple
        """

        result = dict_filter(self.simple_dict, {
            'b': ()
        })

        self.assertEqual(result, {'b': (2, 4, 8, 16)})


    def test_tuple_indices(self):
        """
        Test that a tuple of ints returns indexed values in tuple
        """

        result = dict_filter(self.simple_dict, {
            'b': (1, 0, -1, 2, -2)
        })

        self.assertEqual(result, {'b': (4, 2, 16, 8, 8)})


    def test_tuple_indices_index_error(self):
        """
        Test that filtering for indices out of range raises an index error
        """

        with self.assertRaises(IndexError):

            result = dict_filter(self.simple_dict, {
                'b': (30,)
            })

            print(result)


    def test_tuple_indices_index_error(self):
        """
        Test that filtering for indices out of range raises an index error
        """

        with self.assertRaises(FilterStructureError):

            result = dict_filter(self.simple_dict, {
                'b': ('nope',)
            })

            print(result)


if __name__ == '__main__':
    unittest.main()