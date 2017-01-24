from itertools import combinations

itr, num = raw_input().split()

for i in xrange(1, int(num)+1):
    print "\n".join(''.join(i) for i in list(combinations(sorted(itr),i)))
