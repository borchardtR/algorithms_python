# Title: paths_dfs_iterative.py
# Author: Ryan Borchardt

# This implementation builds off of the code in dfs_iterative.py

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a path exists from a vertex to another vertex (using the same dfs algorithm as in dfs_recursive.py and dfs_iterative.py).
# 2. Determine a path between two connected vertices.  

# Time complexity: Proportional to V + E (see explanation in dfs_iterative.py)
# Space complexity: Proportional to V

# the pathTo() method takes time proportional to the # of vertices on its path, which is a max of V.

# Example:
# python paths_dfs_iterative.py tinyCG.txt ' ' 0

import sys
from chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Paths_dfs:
    def __init__(self, graph, s):
        self.path_array = [None]*graph.V()
        self.marked_array = [False]*graph.V()
        self.s = s
        
        self.dfs(graph, s)
    
    def dfs(self, graph, v):
        self.marked_array[v] = True
        stack = Stack_ResizingArray()
        stack.push(v)
        while stack:
            vertex = stack.pop()

            neighbors_list = graph.adj[vertex]
            for i in neighbors_list:
                if self.marked_array[i] != True:
                    stack.push(i)
                    self.marked_array[vertex] = True
                    self.path_array[i] = vertex
    
    def hasPathTo(self, v):
        return self.marked_array[v]
        
    def pathTo(self,v):
        if not self.hasPathTo(v): return None
        stack = Stack_ResizingArray()
        x = v
        while x != self.s:
            stack.push(x)
            x = self.path_array[x]
        stack.push(self.s)
        return stack
        
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_Array_AdjacencyLists(filename=filename, delimiter=delimiter)
    s = int(sys.argv[3])
    
    paths = Paths_dfs(graph,s)
    
    print(paths.marked_array)
    
    print(paths.path_array)
    
    print(paths.pathTo(0))
    
    # # the pathTo() method returns a stack object (which I have designed to be iterable) so for i in stack_object iterates through the items in each node of the bag
    # for i in range(graph.V()):
    #     string = "0 to " + str(i) +": "
    #     for j in paths.pathTo(i):
    #         if j != i:
    #             string = string + str(j) + "->"
    #         else:
    #            string = string + str(j)
    #     print(string)

if __name__=="__main__":
    main()