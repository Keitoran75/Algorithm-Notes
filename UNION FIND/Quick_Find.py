'''
The idea of the quick find is to identify whether the sets p and q belong are exactly the same.

Cost model
algorithm   initialize  union   find
quick find  N           N       1

Defect: Union too expensive
Takes N^2(quadratic) accesses to process sequence of N union commands on N objects.
'''

class Quick_Find(object):

    def __init__(self, number):
        self.number = number
        # In Python 3, range returns a lazy sequence object - it does not return a list.
        self.id = list(range(self.number))

    # Return a boolean value
    def connected(self, p ,q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.number):
            if self.id[i] == pid:
                self.id[i] = qid


UF = Quick_Find(10)
UF.union(0,5)
print(UF.connected(0,5))
print(UF.connected(1,5))
