import unittest
from dict_filter import dict_filter, FilterStructureError, ExtractDirective

# List of test cases:
#
# - None returns any value
# - Empty list returns any list 
# - List of ints returns indexed values in list
#   - Index error cases
#   - List value error cases
# - Empty tuple returns any tuple
# - Tuple of ints returns indexed values in tuple
#   - Index error cases
#   - Tuple value error cases
# - Empty dictionary returns any dictionary
# - Non-empty dictionary causes recursion into dict value
# - Filter value is a function => Runs function on value
#   - Lambda function
#   - Named function
#   - Built-in functions can take optional second argument with the whole object
# - Builtin Directives
#   - ExtractDirective


class TestFilter(unittest.TestCase):

    simple_dict = {
        'a': 1,
        'b': (2, 4, 8, 16),
        'c': [3, 4, 5]
    }

    nested_dict = {
        'class_info': {
            'subject': 'math',
            'room': 302,
            'teacher': 'Ms Jones'
        },
        'students': [
            {
                'name': 'Frankie',
                'age': 9
            },
            {
                'name': 'Johnny',
                'age': 12
            },
            {
                'name': 'Luigi',
                'age': 11
            }
        ]
    }

    very_nested_dict = {
        'alpha': {
            'bravo': {
                'charlie': {
                    'delta': {
                        'zulu': [1,2,3]
                    }
                }
            }
        }
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


    def test_tuple_indices_structure_error(self):
        """
        Test that filtering for indices out of range raises an index error
        """

        with self.assertRaises(FilterStructureError):

            result = dict_filter(self.simple_dict, {
                'b': ('nope',)
            })


    def test_empty_dict(self):
        """
        Test that an empty dict returns any dict
        """

        result = dict_filter(self.nested_dict, {
            'class_info': {}
        })

        self.assertEqual(result, {'class_info': self.nested_dict['class_info']})


    def test_dict_recursion(self):
        """
        Test that a non-empty dictionary causes recursion into dict value
        """

        result = dict_filter(self.nested_dict, {
            'class_info': {'subject': None}
        })

        self.assertEqual(result, {'class_info': {'subject': 'math'}})


    def test_function_lambda(self):
        """
        Test that a lambda function in the filter runs that function on the dict value
        """

        result = dict_filter(self.nested_dict, {
            'students': lambda x: [student['name'] for student in x]
        })

        self.assertEqual(result, {'students': ['Frankie', 'Johnny', 'Luigi']})


    def test_function_named(self):
        """
        Test that a named function in the filter runs that function on the dict value
        """

        def age(student):
            return student['age']

        result = dict_filter(self.nested_dict, {
            'students': lambda x: [age(student) for student in x]
        })

        self.assertEqual(result, {'students': [9, 12, 11]})


    def test_function_builtin(self):
        """
        Test that a builtin function in the filter runs that function on the dict value
        """

        result = dict_filter(self.nested_dict, {
            'students': len
        })

        self.assertEqual(result, {'students': 3})


    def test_function_two_args(self):
        """
        Test that a function that takes two args in the filter runs that function on the dict value and whole object
        """

        result = dict_filter(self.nested_dict, {
            'students': lambda x, base: [f"{student['name']} {base['class_info']['subject']}" for student in x]
        })

        self.assertEqual(result, {'students': ['Frankie math', 'Johnny math', 'Luigi math']})


    def test_extract_directive(self):
        """
        Test that an ExtractDirective pulls data out up out of a set of nested dicts
        """

        result = dict_filter(self.very_nested_dict, {
            'alpha': ExtractDirective('bravo', 'charlie', 'delta', 'zulu')
        })

        self.assertEqual(result, {'alpha': [1,2,3]})



if __name__ == '__main__':
    unittest.main()