# dict_filter
A simple library for extracting multiple values from a large dictionary or JSON object


## Examples

	from dict_filter import dict_filter

	ex_dict = {
		'a': 1,
		'b': 2,
		'c': [3, 4, 5]
	}

	result = dict_filter(ex_dict, {
		'a': None,
		'c': []
	})

	print(result)

	# Prints {'a': 1, 'c': [3, 4, 5]}




- None returns any value
- Empty list returns any list
- List of ints returns indexed values in list
  - Index error cases
- Empty tuple returns any tuple
- Tuple of ints returns indexed values in tuple
  - Index error cases
- Empty dictionary returns any dictionary
- Non-empty dictionary causes recursion into dict value
- Filter value is a function => Runs function on value
  - Lambda function
  - Named function
  - Built-in function

TODO: 

- Different behavior on index error? Ignore or warn?
- Fill in docs and examples