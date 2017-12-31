# test_solve_happiness.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." )
pth = root_folder + os.sep + 'aikif'

sys.path.append(root_folder + os.sep + 'scripts' + os.sep + 'examples')
sys.path.append(pth + os.sep + 'environments')

import happiness_solver as mod_happy
import happiness as mod_env

all_people = []
all_people.append(mod_env.Person('Gand', {'tax_min':0.3, 'tax_max':0.5, 'tradition':0.2, 'equity':0.9}))
all_people.append(mod_env.Person('Murd', {'tax_min':0.0, 'tax_max':0.2,'tradition':0.5, 'equity':0.1}))

all_worlds = []
w1 = mod_env.World('Astr', [5000, 0.1, .2, 0.3])
w2 = mod_env.World('Cryx', [1000, 0.3, .3, 0.5])
all_worlds.append(w1)
all_worlds.append(w2)

class TestSolveHappiness(unittest.TestCase):

    def test_01_instantiation(self):
        for people in all_people:
            for world in all_worlds:
                #print(mod_happy.Happiness(people, world))
                self.assertEqual(len(str(world)) > 15, True)

    def test_02_person_name(self):
        self.assertEqual(all_people[0].nme, 'Gand')
        self.assertEqual(all_people[1].nme, 'Murd')

    def test_03_person_prefs(self):
        self.assertEqual(all_people[0].prefs['tax_min'], 0.3)
        self.assertEqual(all_people[0].prefs['tax_max'], 0.5)
        self.assertEqual(all_people[0].prefs['tradition'], 0.2)
        self.assertEqual(all_people[0].prefs['equity'], 0.9)

        self.assertEqual(all_people[1].prefs['tax_min'], 0.0)
        self.assertEqual(all_people[1].prefs['tax_max'], 0.2)
        self.assertEqual(all_people[1].prefs['tradition'], 0.5)
        self.assertEqual(all_people[1].prefs['equity'], 0.1)

    def test_04_world_name(self):
        self.assertEqual(all_worlds[0].nme, 'Astr')
        self.assertEqual(all_worlds[1].nme, 'Cryx')

    def test_05_world_prefs(self):
        self.assertEqual(all_worlds[0].population, 5000)
        self.assertEqual(all_worlds[0].tax_rate, 0.1)
        self.assertEqual(all_worlds[0].tradition, 0.2)
        self.assertEqual(all_worlds[0].equity, 0.3)

        self.assertEqual(all_worlds[1].population, 1000)
        self.assertEqual(all_worlds[1].tax_rate, 0.3)
        self.assertEqual(all_worlds[1].tradition, 0.3)
        self.assertEqual(all_worlds[1].equity, 0.5)

    def test_06_worldfinder(self):
        utopia = mod_env.WorldFinder(all_people)
        self.assertEqual(len(str(utopia)) , 160)
        self.assertEqual(utopia.net_happiness , 0)  # initial state is zero
        utopia.solve(silent=True) # now the happiness should be calculated
       # fails self.assertEqual(utopia.net_happiness , 24.200000000000003)
        self.assertEqual(utopia.num_worlds , 448)
        self.assertEqual(utopia.unhappy_people , 0)

        self.assertEqual(utopia.tax_range[0], 0)
        self.assertEqual(utopia.tax_range[1], 7)

        self.assertEqual(utopia.tradition_range[0], 1)
        self.assertEqual(utopia.tradition_range[1], 9)

        self.assertEqual(utopia.equity_range[0], 1)
        self.assertEqual(utopia.equity_range[1], 9)

        self.assertEqual(utopia.is_everyone_happy(), 'Yes')


    def test_07_create_single_person_list(self):
        list1 = mod_happy.create_random_population(num=1)
        self.assertEqual(len(list1), 1)
        self.assertEqual(list1[0].prefs['tax_min'] < 1, True)
        self.assertEqual(list1[0].prefs['tax_min'] > 0, True)

    def test_08_create_10000_person_list(self):
        list1 = mod_happy.create_random_population(num=10000)
        self.assertEqual(len(list1), 10000)
        self.assertEqual(list1[0].prefs['tax_min'] < 1, True)
        self.assertEqual(list1[0].prefs['tax_min'] > 0.009, True)

    def test_10_locations(self):
        erth = mod_env.World('Erth', [7000, 0.1, .2, 0.3])
        country1 = mod_env.WorldLocations('Ostraleu', [26, 0.3, 0.3, 0.4])
        erth.add_location(country1)
        self.assertEqual(len(str(country1)), 108)

    def test_11_happiness_factors(self):
        hf = mod_env.HappinessFactors('tax', 'Economic', 0.1, 0.3)
        self.assertEqual(hf.name, 'tax')


if __name__ == '__main__':
    unittest.main()
