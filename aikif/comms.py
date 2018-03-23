#!/usr/bin/python3
# coding: utf-8
# comms.py

import cls_log as mod_log
import config as mod_cfg


lg = mod_log.Log(mod_cfg.fldrs['log_folder'])
lg.record_process('comms.py', 'Initialing Comms...')


class CommsManager(object):
    """
    overall manager to handle all channels
    """
    def __init__(self):
        self.channels = []

    def __str__(self):
        res = ' /---- CommsManager -------------------------- \n'
        for c in self.channels:
            res += '|  channel : ' + str(c) + '\n'
        res += '\---------------------------------------------\n'
        return res


    def add_channel(self, channel, pwd_hash):
        """
        adds a channel, but must have authenication
        """
        if channel.pwd_hash == pwd_hash:
            self.channels.append(channel)
            lg.record_process('comms.py', 'Added channel ' + channel.name)

            return True
        else:
            lg.record_process('comms.py', 'ERROR - wrong hash for channel ' + channel.name)
            return False


class Channel(object):
    """
    handles a single channel like audio input, output, sensors
    """
    def __init__(self, name, pwd_hash):
        self.name = name
        self.pwd_hash = pwd_hash
        self.inc_msg = 0



    def __str__(self):
        res = self.name
        res += ' : ' + str(self.inc_msg) + ' incoming messages'
        return res
