# puzzle_missions_canninballs.py   written by Duncan Murray  10/1/2015



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


"""

action = {'2m', '1m1c', '2c'}
goal = {'LEFT'=0, 'RIGHT'='3m'}
cost = 1    # same for any action






