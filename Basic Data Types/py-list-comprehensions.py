width = int(raw_input())
length = int(raw_input())
height = int(raw_input())
limit = int(raw_input())

wlist = []
llist = []
hlist = []

for i in range(0, width+1):
    wlist.append(i)

for i in range(0, length+1):
    llist.append(i)

for i in range(0, height+1):
    hlist.append(i)

list = []

for x in wlist:
    for y in llist:
        for z in hlist:
            if wlist[x] + llist[y] + hlist[z] != limit:
                list.append([x,y,z])

print list
