# example_solve_happiness.py   written by Duncan Murray 8/2/2015


def main():
    all_people = []
    all_people.append(Person('Gand', {'tax_min':0.3, 'tax_max':0.5, 'tradition':0.2, 'equity':0.9}))
    all_people.append(Person('Murd', {'tax_min':0.0, 'tax_max':0.2,'tradition':0.5, 'equity':0.1}))
    
    utopia = WorldFinder(all_people)
    utopia.solve()
    print(utopia)
            
class World():
    """
    define a 'world' that all the population live it
    """
    def __init__(self, nme, population, tax_rate, tradition, equity):
        self.nme = nme
        self.population = population
        self.tax_rate = tax_rate
        self.tradition = tradition
        self.equity = equity
        
    def __str__(self):
        res = '\n----- WORLD SUMMARY for : ' + self.nme + ' -----\n'
        res += 'population = ' + str( self.population) + '\n'
        res += 'tax_rate   = ' + str( self.tax_rate) + '\n'
        res += 'tradition  = ' + str( self.tradition) + '\n'
        res += 'equity     = ' + str( self.equity) #+ '\n'
        return res

class WorldFinder():
    """
    Class to iterate through list of worlds (randomly generated
    or using a solver / bit fit algorithm) to try and find the 
    best set of parameters for a world to make all people happy.
    """
    def __init__(self, all_people):
        self.all_people = all_people
        self.net_happiness = 0
        self.num_worlds = 0
    
    def __str__(self):
        res = '\n   === World Finder Results ===\n'
        res += 'Worlds tested  = ' + str(self.num_worlds) + '\n'
        res += 'Best happiness = ' + str(self.net_happiness) + '\n'
        return res
        
    def solve(self, max_worlds=10000):
        """
        find the best world to make people happy 
        """
        num_worlds = 0
        for tax_rate in range(1,5, 1):
            for equity in range(3,8):
                for tradition in range(3,8):
                    num_worlds += 1
                    if num_worlds > max_worlds:
                        break
                    w = World(str(num_worlds).zfill(6), 5000, tax_rate/10, tradition/10, equity/10)
                    world_happiness = 0
                    for person in self.all_people:
                        wh = Happiness(person, w)
                        world_happiness += wh.rating
                    if world_happiness > self.net_happiness:
                        self.net_happiness = world_happiness
                        print('found better world - ' + w.nme + ' = ' + str(world_happiness))
         
class Happiness():
    """
    abstract to manage the happiness calculations
    """
    def __init__(self, person, world):
        self.person = person
        self.world = world
        self.rating = 0
        self.calculate()
        
    def __str__(self):
        """ 
        return happiness rating as description 
        """
        res = self.person.nme + ' is ' 
        if self.rating > 50:
            res += 'Very Happy'
        elif self.rating > 25: 
            res += 'Happy'
        elif self.rating > 5: 
            res += 'Slightly Happy'
        elif self.rating > -5: 
            res += 'Indifferent'
        elif self.rating > -25: 
            res += 'Slightly Unhappy'
        elif self.rating > -50: 
            res += 'Unhappy'
        else:
            res += 'Very Unhappy'
            
        res += ' in ' + self.world.nme + ' (' + str(self.rating) + ')' 
        return res
            
    def calculate(self):
        """
        calculates the estimated happiness of a person
        living in a world
        """
        self.rating = 0
        self._update_pref(self.person.prefs['tax_min'], self.person.prefs['tax_max'], self.world.tax_rate)
        self._update_pref(self.person.prefs['tradition'], self.person.prefs['tradition'], self.world.tradition)
        self._update_pref(self.person.prefs['equity'], self.person.prefs['equity'], self.world.equity)
        
    def _update_pref(self, min, max, cur):
        """
        update the self rating based on the parameters.
        If min max is a range (ie not equal) then add fixed value
        to rating depending if current value is in range, otherwise
        compare distance away from min/max (same value)
        """
        if min == max:
            self.rating -= int(abs(min - cur)*100) / 10
        else:
            if min <= cur:
                self.rating += (int(abs(min - cur)*10)) + 10
            else:
                self.rating -= (int(abs(min - cur)*10)) + 10
            if max >= cur:
                self.rating += (int(abs(max - cur)*10)) + 10
            else:
                self.rating -= (int(abs(max - cur)*10)) + 10

    
class Person():
    def __init__(self, nme, prefs):
        self.prefs = prefs
        self.nme = nme

    def __str__(self):
        res = 'Preferences for ' + self.nme + '\n'
        for k in self.prefs:
            res += k + '  = ' + str(self.prefs[k]) + '\n'
        return res


if __name__ == '__main__':
    main()
