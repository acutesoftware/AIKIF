# test_environment.py

import unittest
import aikif.environments.environment as mod_env

class TestEnvironment(unittest.TestCase):
    
    def test_01_instantiation(self):
        e = mod_env.Environment('unit_test')
        self.assertEqual(str(e), 'Environment: unit_test\n')

        
if __name__ == '__main__':
    unittest.main()