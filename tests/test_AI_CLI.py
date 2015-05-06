# test_AI_CLI.py

import unittest
import sys
import os
import aikif.AI_CLI as mod_cli

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")

class AiCliTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.raw = 'blah'
        self.cli = mod_cli.AICLI('test', False)  # dont autostart CLI
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    def test_01_params_all_commands(self):
        self.assertEqual(len(self.cli.all_commands) > 4, True)  # check for at least 5 commands
        self.assertEqual(self.raw, 'blah')

    def test_02_get_command(self):
        txt = self.cli.get_command('ADD', 'test_02_blah')
        self.assertEqual(txt, 'test_02_blah')
        
    def test_02_show_output(self):
        txt = self.cli.show_output('Dont Print This', 'Function_Return')
        self.assertEqual(txt, 'Dont Print This')
        txt = self.cli.show_output('Print This')  # when printing to console
        self.assertEqual(txt, None)          # there is no return variable
      
    def test_03_show_help(self):
        result, mode = self.cli.process('help', 'COMMAND')
        self.assertEqual(mode, 'COMMAND')   # make sure we stay in command mode
        self.assertEqual(result, '')   # No result returned when showing help
        
    def test_04_enter_add_mode(self):
        result, mode = self.cli.process('add', 'COMMAND')
        self.assertEqual(mode, 'ADD')  
        self.assertEqual(result, 'Entering Add mode') 
        
    def test_05_add_data(self):
        result, mode = self.cli.process('some raw data', 'ADD')
        self.assertEqual(mode, 'ADD')  
        self.assertEqual(result, 'Added some raw data') 
        
    def test_06_exit_add_mode(self):
        result, mode = self.cli.process('cmd', 'ADD')
        self.assertEqual(mode, 'COMMAND')  
        self.assertEqual(result, '')    # No result when returning to command mode
    
    def test_09_exit_program(self):
        with self.assertRaises(SystemExit) as cm:
            result, mode = self.cli.process('quit', 'COMMAND')
        self.assertEqual(cm.exception.code, 0)
         
    def test_11_full_sequence01(self):
        # individual functions have already passed tests
        # so these sections test complex data scenarios.
         
        self.cli.process('The sky is blue', 'ADD')
        self.cli.process('The grass is green', 'ADD')
        self.cli.process('water flows down', 'ADD')
        
        
        
if __name__ == '__main__':
    unittest.main()