# puzzle_missions_canninballs.py  written by Duncan Murray  18/1/2015

"""
On one bank of a river are three missionaries (black triangles) 
and three cannibals (red circles). There is one boat available 
that can hold up to two people and that they would like to use 
to cross the river. If the cannibals ever outnumber the 
missionaries on either of the rivers banks, the missionaries 
will get eaten. How can the boat be used to safely carry all 
the missionaries and cannibals across the river?

STATE                       Set of <action, state>

(L:3m,3c,b-R:0m,0c) ->  {<2c, (L:3m,1c-R:0m,2c,b)>,
                         <1m1c, (L:2m,2c-R:1m,1c,b)>,
                         <1c, (L:3m,2c-R:0m,1c,b)>}

                         
(L:3m,1c-R:0m,2c,b) ->  {<2c, (L:3m,3c,b-R:0m,0c)>,
                         <1c, (L:3m,2c,b-R:0m,1c)>}                       
              

(L:2m,2c-R:1m,1c,b) ->  {<1m1c, (L:3m,3c,b-R:0m,0c)>,
                         <1m, (L:3m,2c,b-R:0m,1c)>}


[(3, 2, 0), (2, 2, 0), (3, 1, 0)]
[(3, 3, 1)]
[(3, 2, 1), (3, 3, 1)]
[(3, 3, 1)]
[(2, 2, 0), (3, 1, 0), (3, 0, 0)]
[(3, 1, 1), (3, 2, 1)]
[(3, 0, 0), (1, 1, 0)]
[(2, 2, 1), (3, 1, 1)]
[(1, 1, 0), (0, 2, 0)]
[(0, 3, 1), (2, 2, 1)]
[(0, 2, 0), (0, 1, 0)]
[(1, 1, 1), (0, 2, 1), (0, 3, 1)]
[(0, 1, 0), (0, 0, 0)]
[(0, 1, 0)]
[(0, 1, 1), (1, 1, 1), (0, 2, 1)]
[(0, 0, 0)]
Took 12 trips for 3 missionaries and 3 canniballs
 /-----------|-----------\
| Left Bank  | Right Bank |
 \-----------|-----------/
| mmmccc     |            |
| mmcc       | mc         |
| mmmcc      | c          |
| mmm        | ccc        |
| mmmc       | cc         |
| mc         | mmcc       |
| mmcc       | mc         |  <-- duplicate!! TO FIX
| cc         | mmmc       |
| ccc        | mmm        |
| c          | mmmcc      |
| mc         | mmcc       |
|            | mmmccc     |


Took 12 trips for 3 missionaries and 3 canniballs
 /-----------|-----------\
| Left Bank  | Right Bank |
 \-----------|-----------/
| mmmccc     |            |
| mmcc       | mc         |
| mmmcc      | c          |
| mmm        | ccc        |
| mmmc       | cc         |
| mc         | mmcc       |
| mmcc       | mc         |
| cc         | mmmc       |
| ccc        | mmm        |
| c          | mmmcc      |
| mc         | mmcc       |
|            | mmmccc     |

Took 6 trips for 2 missionaries and 2 canniballs
 /-----------|-----------\
| Left Bank  | Right Bank |
 \-----------|-----------/
| mmcc       |            |
| mc         | mc         |
| mmc        | c          |
| c          | mmc        |
| mc         | mc         |
|            | mmcc       |

Took 20 trips for 7 missionaries and 4 canniballs
 /-----------|-----------\
| Left Bank  | Right Bank |
 \-----------|-----------/
| mmmmmmmcccc|            |
| mmmmmmccc  | mc         |
| mmmmmmmccc | c          |
| mmmmmccc   | mmc        |
| mmmmmmccc  | mc         |
| mmmmmcc    | mmcc       |
| mmmmmccc   | mmc        |
| mmmmcc     | mmmcc      |
| mmmmmcc    | mmcc       |
| mmmmc      | mmmccc     |
| mmmmcc     | mmmcc      |
| mmmc       | mmmmccc    |
| mmmmc      | mmmccc     |
| mmm        | mmmmcccc   |
| mmmc       | mmmmccc    |
| mm         | mmmmmcccc  |
| mmm        | mmmmcccc   |
| m          | mmmmmmcccc |
| mm         | mmmmmcccc  |
|            | mmmmmmmcccc|
"""

import aikif.lib.cls_plan_search as mod_plan


def main():
    missionaries = int(eval(input('how many missionaries (e.g. 1-9, start with 3)')))
    canniballs =   int(eval(input('how many canniballs  (e.g. 1-9, start with 3)')))
    result = solve(missionaries,canniballs)
    if not result: 
        print(('No path found for ' + str(missionaries) + ' missionaries and '  + str(canniballs) + ' canniballs'))
    else:
        paths = decode_paths_from_results(result, missionaries, canniballs)
        show_results(paths, missionaries,canniballs)

def decode_paths_from_results(result, m,c):
    paths = []
    for node in result:
        paths.append([(node[0],node[1]),(m-node[0],c-node[1])])
    return paths
        
def show_results(result, missionaries,canniballs):
    print(('Took ' + str(len(result)) + ' trips for ' + str(missionaries) + ' missionaries and '  + str(canniballs) + ' canniballs' ))
    print(' /-----------|-----------\\')
    print('| Left Bank  | Right Bank |')
    print(' \-----------|-----------/')
    min_spacing = 11
    if missionaries + canniballs + 1 > min_spacing:
        min_spacing = missionaries + canniballs + 1
    for num, p in enumerate(result):
        displ = '| '
        for bank in p:
            side = ''
            for _ in range(bank[0]):
                side += 'm'
            for _ in range(bank[1]):
                side += 'c'
            displ += side.ljust(min_spacing, ' ') + '| '
        displ += ''  
        print(displ)
        print((num, p))
        

def boat_on_left_bank(node):
    """
    Extracts the boat part (3rd element) and
    returns true (1) if boat is on left bank
    or 0 (false) if boat is on right bank
    """
    boat = node[2]
    mult = int((boat-.5)*2) 
    return boat, mult


def parse_miss_cann(node, m, c):
    """
    extracts names from the node to get 
    counts of miss + cann on both sides
    """
    if node[2]:
        m1 = node[0]
        m2 = m-node[0]
        c1 = node[1]
        c2 = c-node[1]
    else:
        m1=m-node[0]
        m2=node[0]
        c1=c-node[1]
        c2=node[1]
    
    return m1, c1, m2, c2

def pick_next_boat_trip(node, m, c, frontier):
    """ 
    based on current situation, pick who
    gets transported next, and return the path
    NOTE - improvement here as there are often
    duplicate paths or backtracking, e.g.
    """
    next_path = []
    cur_path = []
    boat, mult = boat_on_left_bank(node)
    shore = 1 - boat
    m1, c1, m2, c2 = parse_miss_cann(node, m, c)
    if (m1 - 1 >= c1 or m1 == 1) and (m2 + 1 >= c2) and (m1 > 0):
        cur_path = (node[0]-mult,node[1], shore)
        if cur_path not in frontier:
            next_path.append(cur_path)

    if (m1 >= c1-1 or m1 == 0) and (m2 -1 >= c2 or m2 == 0) and ( c1 > 0):
        cur_path = (node[0],node[1]-mult, shore)
        if cur_path not in frontier:
            next_path.append(cur_path)
        
    if (m1 >= c1) and (m2 >= c2) and (m1 > 0) and (c1 > 0):
        cur_path = (node[0]-mult,node[1]-mult, shore)
        if cur_path not in frontier:
            next_path.append(cur_path)
        
    if (m1 - 2 >= c1 or m1 == 2) and (m2 >= c2 or m2 == 0) and (m1 > 1):
        cur_path = (node[0]-(mult*2),node[1], shore)
        if cur_path not in frontier:
            next_path.append(cur_path)
        
    if (m1 >= c1 - 2 or m1 == 0) and (m2 >= c2 + 2 or m2 == 0) and (c1 > 1):
        cur_path = (node[0],node[1]-(mult*2), shore)
        if cur_path not in frontier:
            next_path.append(cur_path)

    #print(next_path)    
    return next_path
    
def solve(m,c):
    """
    run the algorithm to find the path list
    """
    G={ (m,c,1):[] }
    frontier=[ (m,c,1) ]  # 1 as boat starts on left bank 
    while len(frontier) > 0:
        hold=list(frontier)
        for node in hold:
            newnode=[]
            frontier.remove(node)
            newnode.extend(pick_next_boat_trip(node, m,c, frontier))
            for neighbor in newnode:
                if neighbor not in G:
                    G[node].append(neighbor)
                    G[neighbor]=[node]
                    frontier.append(neighbor)
    return mod_plan.find_path_BFS(G,(m,c,1),(0,0,0))

if __name__ == '__main__':
    main()

