# Title: transitive_closure.py
# Author: Ryan Borchardt

# This class extends the functionality of directed graphs to be able to:
# 1. Determine if a directed path from any given vertex to any other given vertex exists (all-pairs reachability)

# The constructor take quadratic time and subsequent calls after to reachable() take constant time.

# The constructor take V*(V+E) time:
# V calls to constructor of Directed_DFS() which takes V+E time

# Takes space proportional to V^2 (V references to V Directed_DFS objects of size V)

# Example:
# python transitive_closure.py tinyDG.txt ' '


import sys
from chapter_4.directed_graphs.digraph import Digraph
from chapter_4.directed_graphs.directed_dfs import Directed_DFS

class Transitive_Closure:
    def __init__(self, digraph):
        self.array_directed_dfs = []
        
        for i in range(digraph.V()):
            self.array_directed_dfs.append(Directed_DFS(digraph,i))
    def reachable(self, v, w):
        return self.array_directed_dfs[v].marked(w)

        



def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    
    tc = Transitive_Closure(digraph)
    
    print(tc.reachable(6,1))
    print(tc.reachable(8,4))
    print(tc.reachable(4,12))

if __name__=="__main__": main()