# puzzle_missions_canninballs.py 

"""
On one bank of a river are three missionaries (black triangles) 
and three cannibals (red circles). There is one boat available 
that can hold up to two people and that they would like to use 
to cross the river. If the cannibals ever outnumber the 
missionaries on either of the river’s banks, the missionaries 
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

Took 14 trips for 4 missionaries and 4 canniballs
 /-----------|-----------\
| Left Bank  | Right Bank |
 \-----------|-----------/
| mmmmcccc   |            |
| mmmccc     | mc         |
| mmmmccc    | c          |
| mmmmc      | ccc        |
| mmmmcc     | cc         |
| mmmm       | cccc       |
| mmmmc      | ccc        |
| mmc        | mmccc      |
| mmcc       | mmcc       |
| cc         | mmmmcc     |
| ccc        | mmmmc      |
| c          | mmmmccc    |
| mc         | mmmccc     |
|            | mmmmcccc   |

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

def main():
    missionaries = 3 #9 
    canniballs = 3
    result = solve(missionaries,canniballs)
    if not result: 
        print('No path found for ' + str(missionaries) + ' missionaries and '  + str(canniballs) + ' canniballs')
    else:
        paths = decode_paths_from_results(result, missionaries, canniballs)
        show_results(paths, missionaries,canniballs)

def decode_paths_from_results(result, m,c):
    paths = []
    for node in result:
        paths.append([(node[0],node[1]),(m-node[0],c-node[1])])
    return paths
        
def show_results(result, missionaries,canniballs):
    print('Took ' + str(len(result)) + ' trips for ' + str(missionaries) + ' missionaries and '  + str(canniballs) + ' canniballs' )
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
            for m in range(bank[0]):
                side += 'm'
            for c in range(bank[1]):
                side += 'c'
            displ += side.ljust(min_spacing, ' ') + '| '
        displ += ''  
        print(displ)
        #print(num, p)
        
def find_path(Graph,n,m):
    if m not in Graph:
        return None
    if n == m:
        return [m]
    path = [[n]]
    searched = []
    while True:
        j = len(path)
        k = len(Graph[n])
        for i in range(j):
            node = path[i][-1]
            for neighbor in Graph[node]:
                if neighbor not in searched:                    
                    path.append(path[i]+[neighbor])  
                    searched.append(neighbor)
                    if neighbor==m:
                        return path[-1]
        for i in range(j):
            path.pop(0)
    return path

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
            boat, mult = boat_on_left_bank(node)
            m1, c1, m2, c2 = parse_miss_cann(node, m, c)
            if (m1 - 1 >= c1 or m1 == 1) and (m2 + 1 >= c2) and (m1 > 0):
                newnode.append((node[0]-mult,node[1],1-boat))
            if (m1 >= c1-1 or m1 == 0) and (m2 -1 >= c2 or m2 == 0) and ( c1 > 0):
                newnode.append((node[0],node[1]-mult,1-boat))
            if (m1 >= c1) and (m2 >= c2) and (m1 > 0) and (c1 > 0):
                newnode.append((node[0]-mult,node[1]-mult,1-boat))
            if (m1 - 2 >= c1 or m1 == 2) and (m2 >= c2 or m2 == 0) and (m1 > 1):
                newnode.append((node[0]-(mult*2),node[1],1-boat))
            if (m1 >= c1 - 2 or m1 == 0) and (m2 >= c2 + 2 or m2 == 0) and (c1 > 1):
                newnode.append((node[0],node[1]-(mult*2),1-boat))
            for neighbor in newnode:
                if neighbor not in G:
                    G[node].append(neighbor)
                    G[neighbor]=[node]
                    frontier.append(neighbor)
    return find_path(G,(m,c,1),(0,0,0))


main()

