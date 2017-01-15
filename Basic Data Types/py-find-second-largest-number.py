counter = int(raw_input())
sequence = map(int, raw_input().split())
first, second = None, None


for i in range(0, len(sequence)):
    if sequence[i] > first:
        second = first
        first = sequence[i]
    elif first > sequence[i] > second:
        second = sequence[i]

print second
