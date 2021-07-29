'''
Quick find could not handle large scale problem, so quick union is proposed.
Quick union is a lazy method, which means it won't do its job until it's necessary.
    Integer array id[] of size N
    Interpretation: id[i] is parent of i
    Root of i is id[id[id[...id[i]...]]]
Find: Check if p and q have same root
Union: set the id of p's root to the id of q's root

Cost model
algorithm   initialize  union   find
quick find  N           N       1
quick union N           N*      N**
* includes the cost of finding roots
** worst case

Defects: trees could get tall
Find too expensive (could be N array access)
'''

class Quick_Union(object):

    def __init__(self, number):
        self.number = number
        # In Python 3, range returns a lazy sequence object - it does not return a list.
        self.id = list(range(self.number))

    # chase parent pointers until reach root
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        self.id[proot] = qroot

UF = Quick_Union(10)
UF.union(0,5)
print(UF.connected(0,5))
print(UF.connected(1,5))