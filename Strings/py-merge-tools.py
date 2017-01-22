string = raw_input()
k = int(raw_input())
L = []

for i in range(0, len(string), k):
    L.append(string[i:i+k])

for i in range(0, len(L)):
    print "".join(sorted(set(L[i]), key=L[i].index))
