# test_AI_CLI.py

import unittest
import sys
import os
import aikif.AI_CLI as cli

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")

class AiCliTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    def test_01_params_all_commands(self):
        self.assertEqual(len(cli.all_commands) > 4, True)  # check for at least 5 commands

    def test_02_get_command(self):
        txt = cli.get_command('ADD', 'test_02_blah')
        self.assertEqual(txt, 'test_02_blah')
        
    def test_02_show_output(self):
        txt = cli.show_output('Dont Print This', 'Function_Return')
        self.assertEqual(txt, 'Dont Print This')
        txt = cli.show_output('Print This')  # when printing to console
        self.assertEqual(txt, None)          # there is no return variable
      
    def test_03_show_help(self):
        result, mode = cli.process('help', 'COMMAND')
        self.assertEqual(mode, 'COMMAND')   # make sure we stay in command mode
        self.assertEqual(result, '')   # No result returned when showing help
        
    def test_03_add(self):
        result, mode = cli.process('add', 'COMMAND')
        self.assertEqual(mode, 'ADD')  
        self.assertEqual(result, 'Entering Add mode') 
        
        result, mode = cli.process('some raw data', 'ADD')
        self.assertEqual(mode, 'ADD')  
        self.assertEqual(result, 'Added some raw data') 
        
        result, mode = cli.process('cmd', 'ADD')
        self.assertEqual(mode, 'COMMAND')  
        self.assertEqual(result, '')    # No result when returning to command mode
    
    def test_09_exit(self):
        with self.assertRaises(SystemExit) as cm:
            result, mode = cli.process('quit', 'COMMAND')
        self.assertEqual(cm.exception.code, 0)
         
    def test_11_full_sequence01(self):
        result, mode = cli.process('add', 'COMMAND')
        self.assertEqual(result, 'Entering Add mode') 
        
        result, mode = cli.process('The sky is blue', 'ADD')
        result, mode = cli.process('The grass is green', 'ADD')
        result, mode = cli.process('water flows down', 'ADD')
        
        
        
if __name__ == '__main__':
    unittest.main()