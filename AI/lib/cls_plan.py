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
    pass
    
class Desires(object):
    pass

class Intentions(object):
    pass
        
        