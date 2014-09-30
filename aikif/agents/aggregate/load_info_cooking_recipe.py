# load_info_cooking_recipe.py   written by Duncan Murray 30/9/2014

import os
import sys
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..' + os.sep + '..' + os.sep + '..'  )
agt_fldr = os.path.abspath(root_fldr + os.sep + 'aikif' + os.sep + 'agents'  )
data_fldr = os.path.abspath(root_fldr + os.sep + 'data' + os.sep + 'ref'  )

sys.path.append(agt_fldr)  # NOTE - remove this when publishing and use import aikif.agents.agent_map_data
import agent_map_data as mod_map

print('root_fldr = ' + root_fldr)
print('agt_fldr  = ' + agt_fldr)
print('data_fldr = ' + data_fldr)


def main():
    """
    Script to load recipes into the aikif - PROTOTYPE
    """
    test_file = data_fldr + os.sep + 'recipes.csv'
    recipe_map = {
        'name':'recipes', 
        'col_list':['ingredient', 'quant', 'calories'],
        'ingredient':'OBJECT',
        'quant':'VALUE',
        'calories':'VALUE'
    }
    process_list = [
    'fry onions',
    'boil potatoes',
    'broil steak'
    ]
    
    agt = mod_map.AgentMapDataFile('recipes', test_file, recipe_map )
    agt.map_data()
    for proc in process_list:
        agt.add_process(proc)
    print(agt)
        

if __name__ == '__main__':    
    main()

