# lifepim.py

import os
import sys
import aikif.project as mod_prj
import aikif.core_data as mod_core
import aikif.dataTools.cls_datatable as mod_dat

def main():
    fname = 'journal.csv'
    p = mod_prj.Project('Journal Record')
    print(p.nme)

    # Attempt #1 - using DataTable directly (TOK)
    dt = mod_dat.DataTable(fname, ',', col_names=['date', 'category', 'details'])
    dt.add(['2017-12-07', 'Software', 'test online version'])
    dt.add(['2017-06-11', 'Software', 'update readme'])
    dt.add(['2015-05-11', 'Shopping', 'bought jeans'])
    print(dt)
    """
    date	category	details
    11/05/2015	Software	creating LP_ADD_DATA.py to record journal to diary
    11/05/2015	Software	update readme
    11/05/2015	Shopping	bought jeans
    """
    dt.save_csv(fname)


    # attempt #2 using Core DATA  (TOK)
    e = mod_core.CoreDataWhen('Sales Meeting', ['2015-04-11', 'Office', 'Meet with client to discuss custom software'])
    print(e.format_csv())

    # attempt #3 use an Events class to manage it all
    ev = Events(os.getcwd(), 'D', 'DAT')
    ev.add(mod_core.CoreDataWhen('Sales Meeting', ['2014-01-11', 'Office', 'Catchup with client']))
    ev.add(mod_core.CoreDataWhen('Sales Meeting#3', ['2015-03-11', 'Office', 'Catchup with client']))
    ev.add(mod_core.CoreDataWhen('DEV AIKIF - core data', ['2015-05-11', 'Software', 'update TEST - no test for CORE_DATA']))
    ev.add(mod_core.CoreDataWhen('DEV LifePim - core data', ['2015-03-11', 'Software', 'use data for LifePim']))
    ev.add(mod_core.CoreDataWhen('DEV AIKIF - data tools', ['2015-05-11', 'Software', 'fix data tools ']))
    print(ev)

    ev.save()


    txt = 'Catchup' # 'data'
    print('\n Searching for ', txt)
    srch = ev.find(txt)
    for s in srch:
        print(s)   # s.data[2]

class Events():
    """
    class for Diary or LifePIM to handle all events
    """
    def __init__(self, fldr, filename_base, user):
        self.filename_base = filename_base
        self.user = user
        self.fldr = fldr
        self.events = []    # list of events
        self.header = mod_core.CoreDataWhen('Name', ['Date', 'Journal', 'Details'])

    def __str__(self):
        res = ''
        res += ' basename = ' + self.filename_base + '\n'
        res += ' user     = ' + self.user + '\n'
        res += ' fldr     = ' + self.fldr + '\n'
        for e in self.events:
            res += e.format_csv()
        return res

    def get_filename(self, event):
        """
        returns the old style D201505.user format of filename
        """
        return self.fldr + os.sep + self.filename_base + '201505' + '.' + self.user

    def add(self, e):
        self.events.append(e)

    def find(self, txt):
        result = []
        for e in self.events:
            if txt in e.data[2]:
                result.append(e)
                #print(e)
        return result

    def save(self):
        """
        save all events to folder in appropriate files
        NOTE - ONLY APPEND AT THIS STAGE - THEN USE DATABASE
        """

        for e in self.events:
            fname = self.get_filename(e)
            with open(fname, 'a') as f:
                f.write(e.format_csv())

if __name__ == '__main__':
    main()
