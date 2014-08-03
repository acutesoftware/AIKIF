# cls_plan.py

import datetime

class Plan(object):
    """ 
    base class for handling various plans for AIKIF.
    NOTE - this is a stub at this stage and i will need
    to work out exactly how it is going to be implemented
    
    """
        
    def __init__(self, name, dependency):
        self.name = name
        self.id = 1  
        self.success = False
        self.start_date = datetime.datetime.now().strftime("%I:%M%p %d-%B-%Y")
        self.beliefs = Beliefs(self)
        self.desires = Desires()
        self.intentions = Intentions()
        
        
    def __str__(self):
        res = "---==  Plan ==---- \n"
        res += self.name
        return res
        

    def get_name(self):
        return self.name
        
    def generate_plan(self):
        """
        Main logic in class which generates a plan 
        
        """
        print("generating plan... TODO")
        
        
        
    def add_resource(self, name, type):
        """
        add a resource available for the plan
        """
        print("adding resource..." + name + " of type " + type )
        
    def add_constraint(self, name, type, val):
        """
        adds a constraint for the plan
        """
        print("adding constraint..." + name + " of type " + type + " = " + str(val) )

class Beliefs(object):
    def __init__(self, parent_plan):
        self.parent_plan = parent_plan
        self.beliefs = []
        
    def add(self, name):
        self.beliefs.append(name)
    
    def list(self):
        for i, bel in enumerate(self.beliefs):
            print('belief ' + str(i) + ' = ' + bel)
            
    
class Desires(object):
    pass

class Intentions(object):
    pass
        

def TEST():        
    myplan = Plan('new plan', '')
    myplan.beliefs.add('belief0')
    myplan.beliefs.add('belief1')
    myplan.beliefs.add('belief2')
    myplan.beliefs.list()

if __name__ == '__main__':
	TEST()    
    