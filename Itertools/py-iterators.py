from itertools import combinations
N = int(input())
l = input().split()
K = int(input())
c = list(combinations(range(1, N + 1), K))
As = [i + 1 for i in range(len(l)) if l[i] == 'a']

counter = 0
for tup in c:
    if any(x in tup for x in As):
        counter += 1

print(counter / len(c))
