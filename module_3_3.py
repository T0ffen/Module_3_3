def print_params(a=1, b='line', c=True):
    print(a, b, c)


print_params(78, 'brasil')
print_params(None, False, 52)
print_params(27)
print_params()

print_params(b=25)
print_params(c=[1, 2, 3])
print('Functinon print_params(b=25) and print_params(c=[1, 2, 3]) Works')

values_list = [6, 'cloud', True]
values_dict = {'a': 3.1415926535, 'b': 'Blackfire Tourch', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6.02214, 'Infinity Edge']

print_params(*values_list_2, 42)
print('Function print_params(*values_list_2, 42) works')
