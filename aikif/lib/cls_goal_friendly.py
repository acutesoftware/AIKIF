# cls_goal_friendly.py

from cls_goal import Goal

class GoalFriendly(Goal):
    """ 
    goals around friendliness - no idea how to implement at this stage
    """
    def __init__(self, acceptable_damage=10):

        self.maximise = True
        self.cost_life = 0
        self.cost_freedom = 0
        self.cost_damage = acceptable_damage
        self.strategy = []
        
        
    def check_for_success(self):
        res = True
        if self.cost_life > 0:
            res = False
        if self.cost_freedom > 0:
            res = False
        if self.cost_damage > accepted_damage:
            res = False
            
        return res

    def run_plan(self, strategy):
        """ 
        executes a plan by running the passed strategy
        and then updates the local results
        """
        print ("running strategy : " + strategy['name'])
        

    def find_best_plan(self):
        """
        try each strategy with different amounts
        """
        for plan in self.plans:
            for strat in self.strategy:
                run_plan(strat)
                