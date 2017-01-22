string = raw_input()
vowels = 'AEIOU'

kevin_count = 0
stuart_count = 0

for i in range(len(string)):
    if string[i] in vowels:
        kevin_count += len(string)-i
    else:
        stuart_count += (len(string)-i)

if kevin_count > stuart_count:
    print "Kevin", kevin_count
elif kevin_count < stuart_count:
    print "Stuart", stuart_count
else:
    print "Draw"
