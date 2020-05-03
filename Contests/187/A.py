# 16	alanmiller  	19	0:21:16	 0:03:05	 0:03:13	 0:11:10	 0:21:16 (Python solutions for reference)

def a(paths):
    hmap = dict() # stores all cities
    first = dict() # stores departure cities
    for path in paths:
        a, b = path
        if a not in first:
            first[a] = 0

        if b not in hmap:
            hmap[b] = 0
        if a not in hmap:
            hmap[a] = 0

    # destination cities = all cities - departure cities
    return list(set(hmap.keys()) - set(first.keys()))[0]

print(a([["A","Z"]]))
print(a([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))