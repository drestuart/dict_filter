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