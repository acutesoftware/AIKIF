# test_data_structures.py

import unittest
import sys
import os
import aikif.config as mod_cfg
import aikif.toolbox.data_structures as mod_dat

        
class ToolboxDataStructuresTest(unittest.TestCase):

    def test_01_graph(self):
        print('  --== Graph Test ==--')
        g = mod_dat.Graph({'1': ['2','3','4'], '2':['6','7']})
        print('raw graph = ', g)
        self.assertEqual(g.graph,{'2': ['6', '7'], '1': ['2', '3', '4']})
        
    def test_02_get_adjacency_matrix(self):
        g = mod_dat.Graph({'1': ['2','3','4'], '2':['6','7']})
        mat = g.get_adjacency_matrix(True)
        #print('\nget_adjacency_matrix =', mat)
        self.assertEqual(mat, [ [0, 1, 1, 1, 0, 0],
                                [1, 0, 0, 0, 1, 1],
                                [1, 0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0, 0]])
        
    def test_03_node(self):
        #print('\n  --== Node Test ==--')
        trunk = mod_dat.Node('root node') 
        branch1 = mod_dat.Node('1st branch')
        branch2 = mod_dat.Node('2nd branch')
        branch3 = mod_dat.Node('3rd branch')
        trunk.add_link(branch1)
        trunk.add_link(branch2)
        trunk.add_link(branch3)
        self.assertEqual(str(trunk),'root node : ( 3 links)\n  1st branch  2nd branch  3rd branch')

        twig1 = mod_dat.Node('1st twig')
        twig2 = mod_dat.Node('2nd twig')
        branch1.add_link(twig1)
        branch3.add_link(twig2)
        self.assertEqual(str(branch3),'3rd branch : ( 1 links)\n  2nd twig')
        
    def test_04_node_equiv(self):
        #print('\n  --== Node Equiv Test ==--')
        trunk = mod_dat.Node('root node') 
        v1 = mod_dat.Node('Node v1')
        v2 = mod_dat.Node('Node v2')
        self.assertNotEqual(v1, v2)
        
        v3 = v1
        self.assertEqual(v1, v3)
        
        self.assertNotEqual(v1, 'this is not a Note')
        
        trunk.add_link(v1)
        trunk.add_link(v2)
        self.assertEqual(len(trunk.get_children()), 2)
        trunk.add_link(v3)
  
        self.assertEqual(len(trunk.get_children()), 3)
  
        #print('v2.get_parent() = ', v2.get_parent())
        self.assertEqual(v1.get_parent(), trunk)
        self.assertEqual(v2.get_parent(), trunk)
        self.assertEqual(v3.get_parent(), trunk)
  
  
  
  
        
if __name__ == '__main__':
    unittest.main()