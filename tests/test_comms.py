#!/usr/bin/python3
# coding: utf-8
# test_bias.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)

import comms as mod_comms


dummy_comms = [
    {'key':'value'},
]


class CommsTest(unittest.TestCase):
    def tearDown(self):
        unittest.TestCase.tearDown(self)



    def test_01_channel(self):
        #self.comms = mod_bias.Bias(test_metadata)
        ch = mod_comms.Channel('audio', 'F57gj3thddj')
        #cm.add_channel(Channel('TCP', 'Jgfdedfsweewr54'), 'Jgfdedfsweewr54')
        #print(ch)

        self.assertTrue('audio : 0 incoming messages' in str(ch))

    def test_02_comms_manager(self):
        #self.comms = mod_bias.Bias(test_metadata)
        cm = mod_comms.CommsManager()
        self.assertTrue('---- CommsManager ----' in str(cm))
        self.assertTrue(cm.add_channel(mod_comms.Channel('text', '12345'), '12345'))
        self.assertFalse(cm.add_channel(mod_comms.Channel('text', '12345'), 'WRONG HASH'))

        self.assertTrue('channel : text : 0 incoming messages' in str(cm))

        temp_channel = mod_comms.Channel('temp_input', '12345')
        cm.add_channel(temp_channel, '12345')
        self.assertTrue('channel : temp_input : 0 incoming messages' in str(cm))
        self.assertFalse(cm.delete_channel(temp_channel, 'FAKE'))
        self.assertTrue('channel : temp_input : 0 incoming messages' in str(cm))
        self.assertTrue(cm.delete_channel(temp_channel, '12345'))

    def test_03_message(self):
        c_tx =  mod_comms.Channel('RF channel #1', '12345')
        c_rx =  mod_comms.Channel('RF channel #2', '54321')

        m = mod_comms.Message(c_tx, c_rx, 'hello - this is a test', 'content of message')
        self.assertTrue(str(m), 'sender attempting to send message to receiver')
        self.assertTrue(m.send())


if __name__ == '__main__':
    unittest.main()
