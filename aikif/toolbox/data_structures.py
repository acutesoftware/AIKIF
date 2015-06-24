# data_structures.py    written by Duncan Murray 26/1/2015

def TEST():
    """
    self test for various data structures used in aikif
    initially starting with planning structures.
    """
    print('see /tests/test_data_structures.py')
 
        
#----------------------------
# Classes for Data Structures


class Node(object):
    """
    Node data structure
    """
    def __init__(self, name,  data=None):
        """ 
        takes a name and optional data 
        """
        self.name = name
        self.data = data
        self.parent = None
        self.depth = 0
        self.links = []

    def __str__(self):
        res = self.name + ' : ( ' + str(len(self.links)) + ' links)\n'
        for link in self.links:
            res += '  ' + link.name + ''
        return res
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.name == other.name

    def add_link(self, node):
        self.links.append(node)
        node.parent = self
        
    def get_children(self):
        """ returns list of child nodes """
        return self.links
        
    def get_parent(self):
        """ returns list of child nodes """
        return self.parent

 
class Graph(object):
    def __init__(self, graph):
        """ takes a graph definition as input 
        e.g. the following tree is encoded as follows:
        
                 A 
               /   \ 
              B     E 
            / | \    \
           H  C  D    M
        
        would be entered as 
        { 'A': ['B', 'E'],
          'B': ['H', 'C', 'D'],
          'E': ['M']  }
        """
        self.graph = graph
        self.nodes = []
        self.links = []
        self.adj_matrix = []

    def __str__(self):
        """ display as raw data """
        return str(self.graph)
        
    def get_adjacency_matrix(self, show_in_console=False):
        """ return the matrix as a list of lists 
        raw graph =  {'1': ['2', '3', '4'], '2': ['6', '7']}
        6 nodes: ['1', '2', '3', '4', '6', '7']
        5 links: [['1', '2'], ['1', '3'], ['1', '4'], ['2', '6'], ['2', '7']]
        [0, 1, 1, 1, 0, 0]
        [1, 0, 0, 0, 1, 1]
        [1, 0, 0, 0, 0, 0]
        [1, 0, 0, 0, 0, 0]
        [0, 1, 0, 0, 0, 0]
        [0, 1, 0, 0, 0, 0]
        """
        self.links = [[i,j] for i in self.graph for j in self.graph[i]]
        all_nodes = []
        op = [] 
        for node in self.graph:
            all_nodes.append(node)  # to get the root node
            for connection in self.graph[node]:
                all_nodes.append(connection)
        self.nodes = sorted(list(set(all_nodes)))
        if show_in_console is not False:
            print (len(self.nodes), 'nodes:', self.nodes)
            print (len(self.links), 'links:', self.links)
        
        for y in range(len(self.nodes)):
            row = []
            for x in range(len(self.nodes)):
                match = False
                for l in self.links:
                    if self.nodes[x] == l[0] and self.nodes[y] == l[1]:
                        match = True
                    if self.nodes[x] == l[1] and self.nodes[y] == l[0]:
                        match = True
                        
                if match is True:
                    row.append(1)
                else:
                    row.append(0)
                
            op.append(row)
            
        if show_in_console is not False:
            for row in op:
                print(row)
            
        return op
    
    
    
if __name__ == '__main__':
    print('running data_structures.py')
    TEST()  
else:
    print('data_structures imported.py')