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
        self.desires = Desires(self)
        self.intentions = Intentions(self)
        
        
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

class Thoughts(object):
    """ base class for beliefs, desires, intentions simply
    to make it easier to manage similar groups of objects """
    def __init__(self, thought_type):
        self._thoughts = []
        self._type = thought_type
        
    def add(self, name):
        self._thoughts.append(name)
    
    def list(self):
        for i, thought in enumerate(self._thoughts):
            print(self._type + str(i) + ' = ' + thought)
            

    
class Beliefs(Thoughts):
    def __init__(self, parent_plan):
        self.parent_plan = parent_plan
        super().__init__('belief')
        
class Desires(Thoughts):
    def __init__(self, parent_plan):
        self.parent_plan = parent_plan
        super().__init__('desire')

class Intentions(Thoughts):
    def __init__(self, parent_plan):
        self.parent_plan = parent_plan
        super().__init__('intention')
        

def TEST():        
    myplan = Plan('new plan', '')
    myplan.beliefs.add('belief0')
    myplan.beliefs.add('belief1')
    myplan.beliefs.add('belief2')
    myplan.desires.add('desire0')
    myplan.desires.add('desire1')
    myplan.intentions.add('intention0')
    myplan.beliefs.list()
    myplan.desires.list()
    myplan.intentions.list()

if __name__ == '__main__':
	TEST()    
    