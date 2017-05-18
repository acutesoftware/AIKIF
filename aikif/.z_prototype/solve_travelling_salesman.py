# solve_travelling_salesman.py   written by Duncan Murray  20/1/2015

"""


Travelling Salesman problem
===========================


"""

city_distances_csv = 'data_travel_salesman.csv'
     

def main():
    dist = read_distance()
    for i in dist:
        #print(i)
        print((i['town'] + ' is ' + i['dist'] + ' from Bucharest'))
    
def read_distance():
    with open(city_distances_csv, 'r') as file:
        d = []
        for line in file:
            print(line)
            cols = line.split(',')
            town = cols[0]
            dist = cols[1].strip('\n')
            d.append({'town':town, 'dist':dist})
            try:
                print(d)
                pass
            except:
                print('cant print distance')
    return dist
    

if __name__ == '__main__':
    main()	
    