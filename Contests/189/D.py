
# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/discuss/636372/JavaC%2B%2BPython-POJ-1981
def numPoints(self, A, r):
    res = 1
    for (x1, y1), (x2, y2) in itertools.combinations(A, 2):
        d = ((x1 - x2)**2 + (y1 - y2)**2) / 4.0
        if d > r * r: continue
        x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d)**0.5 / (d * 4) ** 0.5
        y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d)**0.5 / (d * 4) ** 0.5
        res = max(res, sum((x - x0)**2 + (y - y0)**2 <= r * r + 0.00001 for x, y in A))
    return res


# points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]]
# r= 2

# Worked for 59/65 cases. For remaining 6 cases, it was off by one.
def my_soln()
    from collections import defaultdict
    plane = defaultdict(int)

    msf = 0
    centres = []
    for point in points:
        # increment all points with R of point by 1
        x, y = point

        for a in range(x - r-1, x + r + 2):
            for b in range(y - r-1, y + r + 2):
                if ((x-a)**2 + (y-b)**2) <= (r*r+0.00001):
                    plane[(a, b)] +=1

                    if plane[(a, b)]>= msf:
                        msf = plane[(a, b)]
                        centres.append((msf, a, b))

    # print(msf)

    # How many divisions to be made of the interval around the integer centre (to explore rational points around it)
    dec = 50   
    tmsf = 0
                                                # I tried tweaking the lower bound/ even included all centres. Even then I was off by one.
    centres = [(c[1], c[2]) for c in centres if (msf-1)<=c[0]<=msf]

    for cent in centres:
        for i in range(-dec, dec+1):
            tmsf = 0
            for point in points:
                x, y = point
                dist = ((x-(cent[0] + i/dec))**2 + (y-(cent[1] + i/dec))**2)
                if dist<=(r*r+0.00001):
                    tmsf += 1
            msf = max(msf, tmsf)

    print(msf)


# https://www.quora.com/What-is-an-algorithm-for-enclosing-the-maximum-number-of-points-in-a-2-D-plane-with-a-fixed-radius-circle


# Idea:
# If there exists a circle C that encloses M points, then by slightly moving C it will touch at least two points. [1]

# So, essentially we just need to check all circles which touch (at least) 2 points:

# For each pair of points in the given set, construct a circle with radius R that touches both points. For each point pair there are at most two such circles.
# For each constructed circle, check for each of the given points is inside it.
# Return the circle that encloses the maximum number of points.
# The runtime of this algorithm is  O(N3)  because there are at most  O(N2)  such circles in step 1, and the linear scan at step 2 takes  O(N)  time.





