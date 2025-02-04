# Title: uf_quickunion.py
# Date: 5/31/2020
# Author: Ryan Borchardt

# QuickUnion 

# The Union Find data structure (also called a disjoint-set forest data structure) allows for storing a collection of disjoint sets of sites.
    # It can be used to efficently answer dynamic connectivity questions like:
        # Is site p connected to site q? If not, merge their sets together. Can be done for a stream of pairs site p and site q.
    # It can answer questions like: is site p connected to site q (ie are site p and site q part of the same set)?
    # Connect p and q (ie merge the their sets together?).
    # What component is site p part of (ie what set is site p part of)? What component is site q part of (ie what set is site q part of)?
    
# The union find data strucure is also used in Kruskal's algorithm for finding the minimum spanning tree of edge-weighted graphs (see Chapter 4.3)

# The test client takes in n pairs of integers.
    # For each pair of integer it establishes a connection between each pair.

# 's' is the number of sites
# 'c' is the number of "connections established" (ie the number of integer pairs in tinyUF.txt / mediumUF.txt)
    # Each of the "connections established" operations corresponds to:
        # 1. Determining if site p and site q are part of the same set (same component)
        # 2. If site p and site q are part of disjoint sets (different components), merge their sets (combine components). 


# The constructor involves s append() operations. append() is constant amortized time, so the order of growth of the constructor is s (linear)
# The method count() takes constant time.
# The method find() depends on the input. 
#   It takes anywhere between constant time (best-case scenario where each site is its own root site / component) and 
#   linear time (worst-case scenario where the site p is at the very bottom of an input that is one component).
# The connected() method uses the find() method so it depends on the input as well. Best case is constant time, worst case linear time.
# The union() method uses the find() method so it depends on the input as well. Best case is constant time, worst case linear time.

# The test client main(): 
    # takes in the number of sites from random input (1, constant)
    # Runs the constructor for UF_quickunion (s, linear)
    # Runs the Union method() c times (beween c*1 and c*s so between linear time and quadratic time)
    # Runs the count() method (1, constant)
    # Runs the connected method twice (between constant (1) and linear time (s)).
    
    # Overall, the test client for quick union has an order of growth between linear and quadratic, depending on the input.

    # tinyUF.txt has 10 sites (s=10) w/ 11 "connections established" operations (c=11).
    # mediumUF.txt has 625 sites (s=625) w/ 900 "connections established" operations (c=900)
    # largeUF.txt has 1 million sites (s=1 mil) w/ 2 million "connections established" operations (c=2 mil)    
    
    # This means that quick union in the best case performs markedly better than quickfind (order of growths c vs s*c) but in the worst case performs similarly (order of growths s*c vs s*c).
    # Therfore, quick union performing better than quick find is not guaranteed.
    
# Example:
# python UF_quickunion.py < tinyUF.txt    
 
import sys
import time
 
class UF_QuickUnion:
    def __init__(self, num_sites):
        self.component_count = num_sites
        self.id = []
        for i in range(num_sites):
            self.id.append(i)
    
    # Add connection between site p and site q (side-effect, no return value)
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        
        if p_root == q_root: return
        else: self.id[p_root] = q_root  
    
    # Find and return the root site for site p (ie find component number for site p)
    def find(self, p):
        while p != self.id[p]: p=self.id[p]
        return self.id[p]
    
    # Return true if site p and site q are from the same component, false if not
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    # Return the number of components
    def count(self):
        return self.component_count
    
    
def main():
    start = time.time()
    # Test client to take in sequence of integers file from standard input
    num_sites = int(sys.stdin.readline())
    
    UF_structure = UF_QuickUnion(num_sites)
    
    for line in sys.stdin:
        pair_list = line.split(" ")
        p = int(pair_list[0])
        q = int(pair_list[1])
        UF_structure.union(p,q)
        
    print(UF_structure.count())
    
    #for i in range(num_sites):
    #    print(UF_structure.find(i))

    print(UF_structure.connected(3,7))
    print(UF_structure.connected(3,8))
    
    finish = time.time()
    
    print(finish-start)

if __name__=="__main__": main()