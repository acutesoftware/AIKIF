# interest_graph.py

# need to map how interested a user is in the objects and concepts
# - check facebook likes, tweets
# - scan files on PC
# - usage logging
# - google docs
# - email (lower rating for recieved)

from pprint import pprint

#local = 'N'
local = 'Y'

if local == 'Y':
    people = []
    with open('T:\\user\\AIKIF\\_PROD\\data\\raw\\contacts.csv', 'r') as f:
        for line in f:
            people.append(line.strip('\n'))
else:
    people = ['Frank', 'Jane', 'Pat']


concepts = ['Movies', 'Music', 'Art', 'Travel', 'Science']
objects = ['Die Hard', 'Mozart', 'Mona Lisa', 'France', 'Solar Power']

raw_likes = {}
#raw_likes['Frank']['Die Hard'] = 1


def main():
    init_graph()
    pprint(raw_likes)
    
    with open('fb_comments.csv', 'r') as f:
        for line in f:
            cols = line.split(',')
            person = cols[0]
            object = cols[1]
            txt = cols[2]
            raw_likes[person, object] = 0.5    # assume partial interest if they comment on it
            raw_likes[person, object] += get_sentiment(txt)
    
    pprint(raw_likes)

def init_graph():
    #raw_likes = {p for p in people
    for person in people:
        for thing in objects:
            raw_likes[person, thing] = 0
        
        #for concept in concepts:
        
  
def get_sentiment(txt):
    """
    will use a proper function for this later
    """
    res = 0
    print('checking sentiment in ', txt)
    positive = ['Loved', 'listening', 'interesting']    
    negative = ['overated', 'hate', 'crap', 'shit', 'rubbish']    
    for word in positive:    
        if word in txt:
            res += 1

    for word in negative:    
        if word in txt:
            res -= 1

    return res
            

main()        