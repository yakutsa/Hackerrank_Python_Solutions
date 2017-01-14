list = []
count = int(raw_input())

for i in range(0, count):
    n = raw_input()
    fn = n.split(" ")[0]

    if fn == "insert":
        position = int(n.split(" ")[1])
        value = int(n.split(" ")[2])
        list.insert(position, value)
    elif fn == "print":
        print list
    elif fn == "remove":
        value = int(n.split(" ")[1])
        list.remove(value)
    elif fn == "append":
        value = int(n.split(" ")[1])
        list.append(value)
    elif fn == "sort":
        list.sort()
    elif fn == "pop":
        list.pop()
    elif fn == "reverse":
        list.reverse()
