import math

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

result = max(orbits, key = (lambda x: x[0] != x[1] and x[0]*x[1]*math.pi))