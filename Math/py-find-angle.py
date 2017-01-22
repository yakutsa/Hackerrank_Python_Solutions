import math

AB = int(raw_input())
BC = int(raw_input())
AC = ((AB * AB) + (BC * BC))**(.5)

first_eq = (AC * AC) + (BC * BC) - (AB * AB)
second_eq = 2 * AC * BC
angle = int(round(math.degrees(math.acos(first_eq/second_eq))))

print str(angle) + u'\N{DEGREE SIGN}'
