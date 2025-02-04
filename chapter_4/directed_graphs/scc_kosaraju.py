# Title: scc_kosaraju.py
# Author: Ryan Borchardt

# Identifies the strongly connected components in a directed graph

# This expands the functionality of digraphs to be able to determine:
# 1. If two given vertices are strongly connected.
# 2. How many strong componenets are in the digraph

# This implementation uses Kosaraju's algorithm and takes time proportional to V+E:
    # 1. Compute the reverse of the digraph (V + E time)
    # 2. Compute the reverse post order of this reversed digraph (V + E time)
    # 3. Run dfs() in vertex order in reverse post order on the original digraph, incrementing the count each time dfs() is called from the constructor (V + E time) 

# Space complexity: proprotional to V + E

# Example:
# python scc_kosaraju.py tinyDG.txt ' '
# python scc_kosaraju.py tinyDG_other.txt ' '
# python scc_kosaraju.py tinyDAG.txt ' '

import sys

from chapter_4.directed_graphs.digraph import Digraph
from chapter_4.directed_graphs.directed_dfs_orderings import Directed_DFS_Orderings


class SCC:
    def __init__(self, digraph):

        self.marked_array = [False]*digraph.V()
        self.id_array = [None]*digraph.V()
        self.count_val = 0
        
        reverse_digraph = digraph.reverse()
        reverse_post_order_stack = Directed_DFS_Orderings(reverse_digraph).reversepostorder()
        print(reverse_post_order_stack)
        
        for vertex in reverse_post_order_stack:
            if not self.marked_array[vertex]:
                self.dfs(vertex, digraph)
                self.count_val+= 1
        
    def dfs(self, v, digraph):
        self.marked_array[v] = True
        self.id_array[v] = self.count_val
        
        points_towards = digraph.adjacent(v)
        
        for vertex in points_towards:
            if not self.marked_array[vertex]:
                self.dfs(vertex, digraph)

        
    def stronglyConnected(self, v, w):
        return self.id_array[v] == self.id_array[w]
        
    def count(self):
        return self.count_val
    
    def id(self, v):
        return self.id_array[v]
        


def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    scc = SCC(digraph)
    
    print(scc.id_array)
    
    print(scc.stronglyConnected(0,5))
    print(scc.stronglyConnected(0,8))
    
    print(scc.count())
    
    print(scc.id(0))
    print(scc.id(5))
    print(scc.id(8))
    
    
if __name__=="__main__": main()