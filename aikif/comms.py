#!/usr/bin/python3
# coding: utf-8
# comms.py


def TEST():
    cm = CommsManager()
    cm.add_channel(Channel('audio', 'F57gj3thddj'), 'F57gj3thddj')
    cm.add_channel(Channel('TCP', 'Jgfdedfsweewr54'), 'Jgfdedfsweewr54')
    print(cm)

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
        # TODO
        if channel.pwd_hash == pwd_hash:
            self.channels.append(channel)
        else:
            print('incorrect password')


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


TEST()
