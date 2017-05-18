# core_data_usage.py

import aikif.core_data as c



#Example showing how the expand/contract work in 
#the core_data object


# Create a root node - optional but handy 
# if working with multiple domains
root = c.Object('Everything')

# add the domains
root.expand('List', ['Food', 'Projects', 'Software'])

# define a domain and instantiate a class (example - you 
# dont do this in day to day usage
food = root.get_child_by_name('Food')

# for the Food - expand it further
food.expand('List', ['Apples', 'Chops', 'Cheese'])
print(('Food = ', food))
print(('  parent of Food = ', food.parent))

# describe a 2nd domain
proj = root.get_child_by_name('Projects')
proj.expand('List', ['Install Shelf', 'AIKIF', 'Prepare Sales Report'])
print(('Projects = ', proj))
shelf = proj.get_child_by_name('Install Shelf')
print(('Shelf = ', shelf))

# contract (or rollup - ie get parent) the shelf
print('Shelf can be contracted to ')
shelf.contract('')

# Events
e = c.Event('Sales Meeting', ['2015-04-11', 'Office', 'Meet with client to discuss custom software'])
print((e.format_csv()))
print((e.format_dict()))


