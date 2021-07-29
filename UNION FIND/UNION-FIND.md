#UNION-FIND
The algorithm we  define should give the result whether two input points: *p* and *q* are connected based on the network.
```python3
UF(int N) # initialize N sites with interger names(0 to N-1)
union(int p, int q) # add connection between p and q
find(p) # component identifier for p (0 to N-1)
connected(int p, int q) # return True if p and q are in the same component
count() #number of components
```
## Dynamic Connectivity
Assume "is connected to" is an *equivalence* relation, which means that it is
* *Reflective*: p is connected to q
* *Symmetric*: If p is connected to q, then q is connected to p
* *Transitive*: If p is connected to q and q is connected to r, then p is connected to r
