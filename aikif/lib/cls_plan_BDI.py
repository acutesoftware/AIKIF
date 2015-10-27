# cls_plan_BDI.py

import datetime

class Plan_BDI(object):
    """ 
    class for handling various plans for AIKIF using
    Belief | Desires | Intentions
    """
        
    def __init__(self, name, dependency):
        self.name = name
        self.id = 1
        self.dependency = dependency
        self.plan_version = "v0.10"
        self.success = False
        self.start_date = datetime.datetime.now().strftime("%I:%M%p %d-%B-%Y")
        self.resources = []
        self.constraint = []
        self.beliefs = Beliefs(self)
        self.desires = Desires(self)
        self.intentions = Intentions(self)
        
        
    def __str__(self):
        res = "---==  Plan ==---- \n"
        res += "name        : " + self.name + "\n"
        res += "version     : " + self.plan_version + "\n"
        for i in self.beliefs.list():
            res += "belief      : " + i + "\n"
        for i in self.desires.list():
            res += "desire      : " + i + "\n"
        for i in self.intentions.list():
            res += "intention   : " + i + "\n"
            
        return res
        

    def get_name(self):
        return self.name
        
    def generate_plan(self):
        """
        Main logic in class which generates a plan 
        """
        print("generating plan... TODO")
        
    def load_plan(self, fname):    
        """ read the list of thoughts from a text file """
        with open(fname, "r") as f:
            for line in f:
                if line != '': 
                    tpe, txt = self.parse_plan_from_string(line)
                    #print('tpe= "' + tpe + '"', txt)
                    if tpe == 'name':
                        self.name = txt
                    elif tpe == 'version':
                        self.plan_version = txt
                    elif tpe == 'belief':
                        self.beliefs.add(txt)
                    elif tpe == 'desire':
                        self.desires.add(txt)
                    elif tpe == 'intention':
                        self.intentions.add(txt)
    
    def save_plan(self, fname):
                
        with open(fname, "w") as f:
            f.write("# AIKIF Plan specification \n")
            f.write("name       :" + self.name + "\n")
            f.write("version    :" + self.plan_version + "\n")
            for txt in self.beliefs.list():
                f.write("belief     :" + txt + "\n")
            for txt in self.desires.list():
                f.write("desire     :" + txt + "\n")
            for txt in self.intentions.list():
                f.write("intention  :" + txt + "\n")
            
    
    def parse_plan_from_string(self, line):
        tpe = ''
        txt = ''
        if line != '':
            if line[0:1] != '#':
                parts = line.split(":")
                tpe = parts[0].strip()
                txt = parts[1].strip()
        return tpe, txt
    
    
    
    def add_resource(self, name, tpe):
        """
        add a resource available for the plan. These are text strings
        of real world objects mapped to an ontology key or programs
        from the toolbox section (can also be external programs)
        """
        self.resources.append([name, tpe])
        
    def add_constraint(self, name, tpe, val):
        """
        adds a constraint for the plan
        """
        self.constraint.append([name, tpe])
        
class Thoughts(object):
    """ base class for beliefs, desires, intentions simply
    to make it easier to manage similar groups of objects """
    def __init__(self, thought_type):
        #print("Thoughts - init: thought_type = " + thought_type + "\n")
        self._thoughts = []
        self._type = thought_type
    
    def __str__(self):
        res = ' -- Thoughts --\n'
        for i in self._thoughts:
            res += i + '\n'
        return res    
    
    def add(self, name):
        self._thoughts.append(name)
    
    def list(self, print_console=False):
        lst = []
        for i, thought in enumerate(self._thoughts):
            if print_console is True:
                print(self._type + str(i) + ' = ' + thought)
            lst.append(thought)
        return lst
    
            
class Beliefs(Thoughts):
    def __init__(self, parent_plan):
        self.parent_plan = parent_plan
        super(Beliefs, self).__init__('belief')
        
class Desires(Thoughts):
    def __init__(self, parent_plan):
        self.parent_plan = parent_plan
        super(Desires, self).__init__('desire')

class Intentions(Thoughts):
    def __init__(self, parent_plan):
        self.parent_plan = parent_plan
        super(Intentions, self).__init__('intention')
        

def TEST():        
    myplan = Plan_BDI('new plan', '')
    myplan.beliefs.add('belief0')
    myplan.beliefs.add('belief1')
    myplan.beliefs.add('belief2')
    myplan.desires.add('desire0')
    myplan.desires.add('desire1')
    myplan.intentions.add('intention0')
    myplan.beliefs.list()
    myplan.desires.list()
    myplan.intentions.list()
    #myplan.save_plan("test_plan.txt")
    #myplan.load_plan("test_plan.txt")
    print(str(myplan))
    
if __name__ == '__main__':
    TEST()  

    
    