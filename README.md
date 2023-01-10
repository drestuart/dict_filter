# dict_filter
A simple library for extracting multiple values from a large dictionary or JSON object

## Basic usage

`dict_filter` uses the contents of a "filter dictionary" to extract values from a source dictionary (or an object in a JSON-encoded string). A simple example:

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

	print(result) # {'a': 1, 'c': [3, 4, 5]}

## Filter values

`dict_filter` looks at each key-value pair in the filter and uses the value to decide what to do with the correpsonding key in the input dictionary.

- None returns any value
- Empty list returns any list
- List of ints returns indexed values in list
- Empty tuple returns any tuple
- Tuple of ints returns indexed values in tuple
- Empty dictionary returns any dictionary
- Non-empty dictionary causes recursion into dict value
- If the filter value is a callable object, the function is run with the value (and optionally the whole dictionary) as inputs. This works with:
  - Lambda functions
  - Named functions
  - Built-in functions

## More examples


