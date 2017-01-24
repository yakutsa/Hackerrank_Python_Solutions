from itertools import permutations

itr, num = raw_input().split()

for j in sorted([''.join(i) for i in list(permutations(itr, int(num)))]):
    print j
