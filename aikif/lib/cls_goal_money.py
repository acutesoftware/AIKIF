# cls_goal_money.py

from aikif.lib.cls_goal import Goal

class GoalMoney(Goal):
    """ 
    goals around money and finance - eg maximise profit / minimize costs
    """
    def __init__(self, maximise=True, current_val=0, target_val=0):
        """
        set maximise = True for class to find maximum money (profits) or
        set to False to minimise the amount of money (eg reduce costs)
        """
        self.current_val = current_val
        self.target_val = target_val
        self.maximise = maximise
        self.strategy = [
            {'name':'Bank Savings', 'interest_pa':0.03, 'min_deposit':1, 'fixed_cost':10.0, 'payable': 30},
            {'name':'Term Deposit', 'interest_pa':0.05, 'min_deposit':5000, 'fixed_cost':100.0, 'payable':364}
        ]
        
        
    def check_for_success(self):
        if self.maximise == True:
            if self.target_val > self.current_val:
                return True
            else:
                return False
        else:
            if self.target_val < self.current_val:
                return True
            else:
                return False

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
                