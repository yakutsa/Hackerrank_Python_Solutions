from itertools import combinations_with_replacement

s, itr = raw_input().split()

print list(combinations_with_replacement(s,itr))
