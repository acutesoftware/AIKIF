# load_info_cooking_recipe.py   written by Duncan Murray 30/9/2014

import os
import sys
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..' + os.sep + '..' + os.sep + '..'  )
agt_fldr = os.path.abspath(root_fldr + os.sep + 'aikif' + os.sep + 'agents'  )
data_fldr = os.path.abspath(root_fldr + os.sep + 'data' + os.sep + 'ref'  )

sys.path.append(agt_fldr)  # NOTE - remove this when publishing and use import aikif.agents.agent_map_data
import agent_map_data as mod_map

def main():
    """
    Script to load recipes into the aikif - PROTOTYPE
    This program should contain mainly data about recipe mappings
    and should be using the AgentMapDataFile class for all code.
    
    Not sure exactly how to implement yet: (c looks best)
    a) force recipes to a standard format and parse (not too useful)
    b) add ingredients and steps as per below (time consuming)
    c) parse it out automatically. Take all the text of a recipe and
    use this as the 'steps' that the human performs. Then parse out the
    list of ingredients into an ingredient table and use that separately.
    
    How is the data saved?
    - ingredients list
    - steps (free form text)
    
    Mapping to aikif?
    - Objects: recipe itself as outcome, plus list of ingredients + utensils
    - Events: 'making the recipe', + individual things to do (eg +10min turn on oven)
    - Locations: buying ingred. source of recipe. location of cooking
    - People: how many to serve, cook, taster
    
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


