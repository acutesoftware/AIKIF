# gui_view_world.py     written by Duncan Murray 10/7/2014

import os
import sys
try:
	import Tkinter as Tkinter
except:
	import tkinter as Tkinter

	
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder)
print(root_folder)
#import AI.agents.agent as agt
			
def usage():
    print("gui_view_world.py - AIKIF script to view a saved map")
    print("Usage:")
    print("   gui_view_world.py filename")
"""
try:                                
    opts, args = getopt.getopt(sys.argv[1:], "f", ["help"])
    print (opts, args)
except getopt.GetoptError:          
	usage()                         
	sys.exit(2)                     
"""
	
fname = root_folder + os.sep + "examples" + os.sep + "test_world.txt"
    
def main():
    """
    view a text file (map) in high resolution
    """
    print("viewing ", fname)
    wrld = read_map(fname)
    for row in wrld:
        #for col in row:
        print(row)
    app = simpleapp_tk(None)
    app.title('Map View')
    app.mainloop()
    
    
    
def read_map(fname):
    """
    reads a saved text file to list
    """
    lst = []
    with open(fname, "r") as f:
        for line in f:
            lst.append(line)
    return lst


class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.appWidth = 1900
        self.appHeight = 900
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()

        self.geometry('%dx%d+%d+%d' % (self.appWidth, self.appHeight, self.screenWidth - self.appWidth - 0, self.screenHeight - self.appHeight - 0))
        self.grid()
        self.update()











    
if __name__ == "__main__":
    main()