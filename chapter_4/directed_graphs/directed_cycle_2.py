# Title: directed_cycle_2.py
# Author: Ryan Borchardt

# Alternate implementation of directed_cycle.py
    # The only difference between the two implementations is where I add and remove vertices from the stack in the code.

# This class extends the functionality of directed graphs to be able to:
# 1. Determine if a cycle exists in the digraph.
# 2. If a cycle exists, list a cycle (just one) in the digraph.

# Time complexity: Proportional to V + E
# Space complexity: Proportional to V 


# Example:
# python directed_cycle_2.py tinyDG.txt ' '
# python directed_cycle_2.py tinyDAG.txt ' ' 


import sys
from chapter_4.directed_graphs.digraph import Digraph
from chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Directed_Cycle:
    def __init__(self, digraph):
        # This is used to keep track of whether a vertex has been encountered or not.
        # This way dfs() will only run at most once for each vertex
        self.marked_array = [False]*digraph.V()
        
        # This array is used to build the cycle_stack
        # For a given index
        self.paths_array = [None]*digraph.V()
        
        # This stack stays empty until a cycle is detected.
        # If a cycle is detected, all of the vertices along the cycle are added to the stack
        # This is done by utilizing the paths_array which stores the previous vertex along its path
        self.cycle_stack = Stack_ResizingArray()
        
        # This array keeps track of whether a vertex is still on the call stack.
        # If we encounter a vertex that is still on the call stack, then we know a cycle exists (similar to how if the end of the string re-encounters the string in the Tremaux maze)
        # The value at a given index is turned to True while it is on the call stack and turned to False when dfs finishes (and it is no longer on the call stack)
        self.onStack = [False]*digraph.V()
        
        for i in range(digraph.V()):
            # This way dfs goes through all vertices even if in different components.
            if not self.marked_array[i]:
                self.onStack[i]=True
                self.dfs(i, digraph)
                self.onStack[i]=False
        
    def dfs(self,v, digraph):
        self.marked_array[v] = True
        for vertex in digraph.adjacent(v):
            # 1.
            # If a cycle has already been detected (and consequently cycle_stack has been built),
            # Then no more calls to dfs() will be added to the call stack and those remaining are quickly finished w/ this return statement.
            if self.hasCycle(): return
            
            # 2.
            # If a vertex has already been encountered, then we don't need to re-search through its neighbors.
            # We only search through the neighbors of a vertex once.
            elif not self.marked_array[vertex]:
                self.paths_array[vertex] = v
                self.onStack[vertex]=True
                self.dfs(vertex, digraph)
                self.onStack[vertex]=False
            
            # 3.
            # If this is a true, a cycle has been detected and we can build the cycle stack to show the cycle.
            elif self.onStack[vertex]:
                self.cycle_stack.push(vertex)
                x = v
                while x != vertex:
                    self.cycle_stack.push(x)
                    x = self.paths_array[x]
                self.cycle_stack.push(vertex)
        
    
    
        
    
    
    def hasCycle(self):
        return not self.cycle_stack.isEmpty()
        
    def cycle(self):
        if not self.hasCycle():
            return None
        else: 
            return self.cycle_stack
        
        



def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    dc = Directed_Cycle(digraph)
    print('Does the digraph have a cycle?', dc.hasCycle())
    print('Cycle in digraph:')
    print(dc.cycle())

    
if __name__=="__main__": main()