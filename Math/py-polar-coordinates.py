import cmath
c = complex(raw_input())

print "\n".join(map(str, cmath.polar(c)))
