def my_soln(coordinates):
    x, y = coordinates[0]
    slope = None
    import math

    for coordinate in coordinates[1:]:
        a, b = coordinate
        
        if slope == None:
            if x-a!=0:
                slope = (y-b)/ (x-a)
            else:
                slope = math.inf
        
        elif slope == math.inf and x-a == 0:
            continue
            
        elif slope!= (y-b)/ (x-a):
            return False
            
    return True

def concise(coordinates):
    # slope of points 1 and 2 must be same as points 2 and 3; Avoids zero division error
    (x0, y0), (x1, y1) = coordinates[: 2]
    return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)

def traingle_area(coordinates):
    for i in range(len(coordinates) - 2):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        x3, y3 = coordinates[i+2]

        # If area of the traingle formed using the 3 points is zero, they lie on the same line
        if 0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) != 0:
            return False
        
    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

print(my_soln(coordinates))
print(concise(coordinates))
print(traingle_area(coordinates))