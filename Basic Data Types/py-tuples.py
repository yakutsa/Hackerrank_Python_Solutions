counter = int(raw_input())
sequence = raw_input().split()
sequence = map(int, sequence)

tuple = tuple(sequence)
print hash(tuple)
