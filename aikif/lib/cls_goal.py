# cls_goal.py

import datetime

class Goal(object):
    """ 
    base class for handling various goals for AIKIF, usually in string format, but
    has methods to load/save and compare.
    name: title of the goal
    id: id of the goal - obtain from Goals class or database
    success: whether the goal has been successful or not
    """
        
    def __init__(self, name='New Goal', plans=None):
        self.name = name
        self.id = 1  
        self.success = False
        self.plans = plans
        self.start_date = datetime.datetime.now().strftime("%I:%M%p %d-%B-%Y")
        
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name
        
    def find_best_plan(self):
        """
        Main logic in class which tries different plans according to a
        strategy (no idea how as yet) on test data, then runs that plan
        to simulate a result
        """
        for plan in self.plans:
            print(("running plan ", plan[0]))
            
        
    def check_for_success(self):
        """ do the checking to see if goal has reached its target
        This is usually overloaded by other classes, and for numerical
        tests is simply if maximise == True:
                            if TARGET > CURRENT:
                                return True
                            else:
                                return False
                        else:
                            if TARGET < CURRENT:
                                return True
                            else:
                                return False
        """
        return False
        
