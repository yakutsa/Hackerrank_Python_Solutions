from itertools import groupby
print " ".join(str((len(list(k)),int(i))) for i,k in groupby(raw_input()))
