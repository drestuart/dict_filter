from dict_filter.filter import dict_filter

# List of test cases:
#
# - None returns any value
# - Empty list returns any list
# - List of ints returns indexed values in list
#   - Index error cases
# - Empty tuple returns any tuple
# - Tuple of ints returns indexed values in tuple
#   - Index error cases
# - Empty dictionary returns any dictionary
# - Non-empty dictionary causes recursion into dict value
# - Filter value is a function => Runs function on value
#   - Lambda function
#   - Named function
#   - Built-in function




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