# game_of_life_console.py
import os
import sys
import time

cur_folder = os.path.dirname(os.path.abspath(__file__)) 
lib_folder = os.path.abspath(cur_folder + os.sep + ".." +  os.sep + "toolbox" )
aikif_folder = os.path.abspath(cur_folder + os.sep + ".."  )

import aikif.toolbox.cls_grid_life as mod_grid
import aikif.cls_log as mod_log
lg = mod_log.Log('')

lg.record_process("Running Game of Life Console...")
os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Example to show AIKIF logging of results.
    Generates a sequence of random grids and runs the
    Game of Life, saving results
    """
    iterations  = 10     # how many simulations to run
    years       = 100    # how many times to run each simulation
    width       = 22     # grid height
    height      = 78     # grid width
    time_delay  = 0.03   # delay when printing on screen
    lg = mod_log.Log('test')
    lg.record_process('Game of Life', 'game_of_life_console.py')
    for _ in range(iterations):
        s,e = run_game_of_life(years, width, height, time_delay, 'N') 
        lg.log_result("Started with " +  str(s) + " cells and ended with " + str(e) + " cells")
        
def run_game_of_life(years, width, height, time_delay, silent="N"):
    """
    run a single game of life for 'years' and log start and 
    end living cells to aikif
    """
    lfe = mod_grid.GameOfLife(width, height, ['.', 'x'], 1)
    set_random_starting_grid(lfe)
    lg.log_source(lfe, 'game_of_life_console.py')
    print(lfe)
    start_cells = lfe.count_filled_positions()
    for ndx, dummy_idx in enumerate(range(years)):
        lfe.update_gol()
        if silent == "N":
            print_there(1,1, "Game of Life - Iteration # " + str(ndx))
            print_there(1, 2, lfe)
            time.sleep(time_delay)
    end_cells = lfe.count_filled_positions()
    return start_cells, end_cells

    
def set_random_starting_grid(lfe):
    """
    generate a random grid for game of life using a 
    set of patterns (just to make it interesting)
    """
    cls_patterns = mod_grid.GameOfLifePatterns(25)
    patterns = cls_patterns.get_patterns()
    for pattern in patterns:
        lfe.set_tile(pattern[0], pattern[1], 1)
#    return patterns
    
def print_there(x, y, text):
    """"
    allows display of a game of life on a console via
    resetting cursor position to a set point - looks 'ok'
    for testing but not production quality.
    """
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()        

main()
