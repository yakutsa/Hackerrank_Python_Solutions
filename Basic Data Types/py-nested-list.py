nlist = []
slist = []
tlist=[]

for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    nlist.append(name) # create name list
    slist.append(score) # create score list

for x in range(0, len(nlist)):
    for y in range(0, len(slist)):
        if x == y:
            tlist.append([nlist[x],slist[y]])

tlist.sort() #sort alphabetically

first, second = 100, 100

#find the second lowest grade
for i in range(0, len(tlist)):
    if tlist[i][1] < first:
        second = first
        first = tlist[i][1]
    elif first < tlist[i][1] < second:
        second = tlist[i][1]

#print the student of second lowest grade
for i in range(0, len(tlist)):
    if second == tlist[i][1]:
        print tlist[i][0]
