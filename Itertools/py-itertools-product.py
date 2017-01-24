# product(A, B) returns the same as ((x,y) for x in A for y in B).
from itertools import product

x = map(int, raw_input().split())
y = map(int, raw_input().split())

print " ".join(str(i) for i in product(x, y))
