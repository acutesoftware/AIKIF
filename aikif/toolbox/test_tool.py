# test_tool.py	
# testing toolbox functionality

def test_function():
	print('hello world')
	return 4
	
	
def sum_even_numbers(numbers):
	return sum([i for i in numbers if i % 2 == 0])
	
def get_min_even_num(numbers):
	return min([i for i in numbers if i % 2 == 0])
		
# other code in test1.py which we dont want to execute
print('test_tool.py has been run' )
	