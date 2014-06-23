# cls_goal_friendly.py

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
		pass = True
		if self.cost_life > 0:
			pass = False
		if self.cost_freedom > 0:
			pass = False
		if self.cost_damage > accepted_damage:
			pass = False
			
        return pass

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
                