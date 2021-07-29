'''
The question becomes how to optimize the performance of the algorithm
One method is called Weighted quick union, which ensures that the tree in quick union won't be too tall. In other words,
the bigger tree is always higher than smaller one. It is guaranteed that on item is too far away from the root.

Data Structure: same as quick union, but maintain extra array sz[i] to count number of objects in the tree rooted at i.

Find: identical to quick-union.
Union: Modify quick-union to:
    Link root of smaller tree to root of larger tree.
    Update sz[] array

Running time:
    Find: takes time proportional to depth of p and q.
    Union: takes constant time, given roots.
Proposition: Depth of any node x is at almost lgN

Cost model
algorithm       initialize  union   find
quick find      N           N       1
quick union     N           N*      N**
Weighted QU     N           lgN*    lgN**
* includes the cost of finding roots
** worst case
'''

class Weighted_Quick_Union(object):

    def __init__(self, number):
        self.number = number
        # In Python 3, range returns a lazy sequence object - it does not return a list.
        self.id = list(range(self.number))

    # chase parent pointers until reach root
    def root(self, i):
        while i != self.id[i]:
            # path compression: try to flatten the tree
            self.id = self.id[self.id[i]]
            i = self.id[i]
        return i

    # get the size of tree contains p
    def sz(self, p):
        return self.id.count(p)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        proot = self.root(p)
        qroot = self.root(q)
        if self.sz(proot) > self.sz(qroot):
            self.id[qroot] = proot
        else:
            self.id[proot] = qroot

UF = Weighted_Quick_Union(10)
UF.union(0,5)
UF.union(5,2)
print(UF.connected(0,5))
print(UF.connected(1,5))
print(UF.id)