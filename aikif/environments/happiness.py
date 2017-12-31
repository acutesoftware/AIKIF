# happiness.py      written by Duncan Murray 20/2/2015

def TEST():
    """
    Modules for testing happiness of 'persons' in 'worlds'
    based on simplistic preferences. Just a toy - dont take seriously

        ----- WORLD SUMMARY for : Mars -----
        population = 0
        tax_rate   = 0.0
        tradition  = 0.9
        equity     = 0.0
        Preferences for Rover
        tax_min  = 0.0
        equity  = 0.0
        tax_max  = 0.9
        tradition  = 0.9

        Rover is Indifferent in Mars (0)
        DETAILS
                    tax: Economic = 0.1 -> 0.3
              tradition: Personal = 0.3 -> 0.9
                 equity: Personal = 0.1 -> 0.9
                 growth: Economic = 0.01 -> 0.09


    """
    w = World('Mars', [0, 0.0, 0.9, 0.0])
    print(w)
    p = Person('Rover', {'tax_min':0.0, 'tax_max':0.9,'tradition':0.9, 'equity':0.0})
    print(p)

    h = Happiness(p,w)
    #h.add_factor(HappinessFactors(name, type, min, max))
    h.add_factor(HappinessFactors('tax', 'Economic', 0.1, 0.3))
    h.add_factor(HappinessFactors('tradition', 'Personal', 0.3, 0.9))
    h.add_factor(HappinessFactors('equity', 'Personal', 0.1, 0.9))
    h.add_factor(HappinessFactors('growth', 'Economic', 0.01, 0.09))
    print(h.show_details())

class World(object):
    """
    define a 'world' that all the population live it
    """
    def __init__(self, nme, params):
        self.nme = nme
        self.population = params[0]
        self.tax_rate = params[1]
        self.tradition = params[2]
        self.equity = params[3]
        self.world_locations = []

    def __str__(self):
        res = '\n----- WORLD SUMMARY for : ' + self.nme + ' -----\n'
        res += 'population = ' + str( self.population) + '\n'
        res += 'tax_rate   = ' + str( self.tax_rate) + '\n'
        res += 'tradition  = ' + str( self.tradition) + '\n'
        res += 'equity     = ' + str( self.equity) #+ '\n'
        return res

    def add_location(self, loc):
        """
        a world can have 0 or many locations - this adds one to the world
        """
        self.world_locations.append(loc)

    def get_population(self):
        pop = 0
        for loc in self.world_locations:
            pop += loc.population
        return pop

class WorldLocations(object):
    """
    This is a subsection of the World with its own parameters
    to allow people to experience maximum happiness (that's the idea anyway)
    """
    def __init__(self, nme, params):
        self.nme = nme
        self.pos_x = 0     # may not use a grid, would be better as a graph
        self.pos_y = 0     # to allow large populations to expand without effect
        self.population = params[0]
        self.tax_rate = params[1]
        self.tradition = params[2]
        self.equity = params[3]

    def __str__(self):
        res = '\n----- WORLD SUMMARY for : ' + self.nme + ' -----\n'
        res += 'population = ' + str( self.population) + '\n'
        res += 'tax_rate   = ' + str( self.tax_rate) + '\n'
        res += 'tradition  = ' + str( self.tradition) + '\n'
        res += 'equity     = ' + str( self.equity) #+ '\n'
        return res

class WorldFinder(object):
    """
    Class to iterate through list of worlds (randomly generated
    or using a solver / bit fit algorithm) to try and find the
    best set of parameters for a world to make all people happy.
    """
    def __init__(self, all_people):
        self.all_people = all_people
        self.net_happiness = 0
        self.num_worlds = 0
        self.unhappy_people = 0
        self.tax_range = (0,7)
        self.tradition_range = (1,9)
        self.equity_range = (1,9)


    def __str__(self):
        res = '\n   === World Finder Results ===\n'
        res += 'Worlds tested        = ' + str(self.num_worlds) + '\n'
        res += 'Best happiness       = ' + str(self.net_happiness) + '\n'
        res += 'Num Unhappy people   = ' + str(self.unhappy_people) + '\n'
        res += 'Tot People in world  = ' + str(len(self.all_people)) + '\n'
        res += 'Everyone happy       = ' + self.is_everyone_happy() + '\n'
        return res

    def is_everyone_happy(self):
        """
        returns text result iff everyone happy
        """
        if self.unhappy_people == 0:
            return 'Yes'
        else:
            return 'No'

    def solve(self, max_worlds=10000, silent=False):
        """
        find the best world to make people happy
        """
        self.num_worlds = 0
        num_unhappy = 0
        for tax_rate in range(self.tax_range[0],self.tax_range[1]):
            for equity in range(self.equity_range[0],self.equity_range[1]):
                for tradition in range(self.tradition_range[0],self.tradition_range[1]):
                    self.num_worlds += 1
                    if self.num_worlds > max_worlds:
                        break
                    w = World(str(self.num_worlds).zfill(6), [5000, tax_rate/10, tradition/10, equity/10])
                    world_happiness = 0
                    num_unhappy = 0
                    for person in self.all_people:
                        wh = Happiness(person, w)
                        world_happiness += wh.rating
                        if wh.rating < 0:
                            num_unhappy += 1
                    if world_happiness > self.net_happiness:
                        self.net_happiness = world_happiness
                        self.unhappy_people = num_unhappy
                        if not silent:
                            print('found better world - ' + w.nme + ' = ' + str(world_happiness) + ' - total unhappy_people = ' + str(self.unhappy_people))

class HappinessFactors(object):
    """
    class for parameters used to calculate happiness
    h = Happiness(p, w)
    h.add_factor(HappinessFactors('tax rate', 0.2, 0.5, 'hi'))
    """
    def __init__(self, name, tpe, mn, mx):
        self.name = name
        self.type = tpe
        self.min = mn
        self.max = mx

    def __str__(self):
        res = self.name.rjust(15) + ': '
        res += self.type + ' = '
        res += str(self.min) + ' -> '
        res += str(self.max) + '\n'
        return res


class Happiness(object):
    """
    abstract to manage the happiness calculations.
    The purpose of this class is to attempt to assign a number
    to a persons happiness in a (limited parameters) world
    Note - original calculation was flat out wrong - just
    because the tax_rate is not ideal doesn't mean the person
    is unhappy, rather that is a desire or preference.
    It does have an influence but the influence needs to be
    scaled right back.

    Options
    Need to have a class of preferences and their weightings,
    so things like death by starvation has high unhappiness but
    wishing you were a flying dragon has a low impact on happiness

    """
    def __init__(self, person, world):
        self.person = person
        self.world = world
        self.factors = []
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

    def show_details(self):
        """
        extended print details of happiness parameters
        """
        res = str(self)
        res += '\nDETAILS\n'
        for f in self.factors:
            res += str(f)

        return res

    def add_factor(self, factor):
        self.factors.append(factor)


    def calculate(self):
        """
        calculates the estimated happiness of a person
        living in a world
        self._update_pref(self.person.prefs['tax_min'], self.person.prefs['tax_max'], self.world.tax_rate)
        self._update_pref(self.person.prefs['tradition'], self.person.prefs['tradition'], self.world.tradition)
        self._update_pref(self.person.prefs['equity'], self.person.prefs['equity'], self.world.equity)
        """
        self.rating = 0
        for f in self.factors:
            self._update_pref(f.min, f.max, self.world.tax_rate)

    def _update_pref(self, lmin, lmax, cur):
        """
        update the self rating based on the parameters.
        If min max is a range (ie not equal) then add fixed value
        to rating depending if current value is in range, otherwise
        compare distance away from min/max (same value)
        """
        rate_of_change_positive = 10
        rate_of_change_negative = 2
        add_positive = 10
        add_negative = 2
        if lmin == lmax:
            self.rating -= int(abs(lmin - cur)*100) / 10
        else:
            if lmin <= cur:
                self.rating += (int(abs(lmin - cur)*rate_of_change_positive)) + add_positive
            else:
                self.rating -= (int(abs(lmin - cur)*rate_of_change_negative)) + add_negative
            if lmax >= cur:
                self.rating += (int(abs(lmax - cur)*rate_of_change_positive)) + add_positive
            else:
                self.rating -= (int(abs(lmax - cur)*rate_of_change_negative)) + add_negative


class Person(object):
    def __init__(self, nme, prefs):
        self.prefs = prefs
        self.nme = nme
        self.values = []

    def __str__(self):
        res = 'Preferences for ' + self.nme + '\n'
        for k in self.prefs:
            res += k + '  = ' + str(self.prefs[k]) + '\n'

        if self.values:
            res += 'Has the following values rated:\n'
            for v in self.values:
                res += ' - ' + v[0].nme + ' = ' + str(v[1]) + '\n'
        return res

    def add_value(self, value, importance):
        """
        add a value that a person believes in and the
        importance of that value to the person (1-100)
        """
        self.values.append([value, importance])


class Value(object):
    """
    A value is an atomic description of something a person
    believes in.
    """
    def __init__(self, nme, desc=''):
        self.desc = desc
        self.nme = nme

    def __str__(self):
        return self.nme + '\n'

    def match_value_to_text(self, text):
        """
        this is going to be the tricky bit - probably not possible
        to get the 'exact' rating for a value. Will need to do sentiment
        analysis of the text to see how it matches the rating. Even that
        sounds like it wont work - maybe a ML algorithm would do it, but
        that requires a large body of text already matched to values - and
        values aren't even defined as far as I have found.

        UPDATE - this could work if we assume values can be single words,
        eg tax=0.3, freedom=0.7, healthcare=0.3, welfare=0.3 etc
        """

        if self.nme in text:

            res = 0.8
        else:
            res = 0.2

        return self.nme + ' = ' + str(res) + ' match against ' + text


if __name__ == '__main__':
    TEST()
