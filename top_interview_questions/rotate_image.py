import itertools
# Most solutions come from here;  https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

def topdown_reverse_swap(image):
    # https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image

    # clockwise rotation: reverse --> swap i,j with j, i (transpose)
    # anticlockwise rotation: swap i,j  with j, i --> reverse

    # reverse
    image = image[::-1]
    # image.reverse()

    # symmetry swap
    n = len(image)
    for i in range(n):
        for j in range(i):
            image[i][j], image[j][i] = image[j][i], image[i][j]
    return image

def topdown_reverse_swap_pythonic(image):
    # zip takes in a bunch of iterables (here our rows). the *operator unpacks the matrix of rows into separate rows.

    # Why [:]?  A = zip(*A[::-1]) just reassigns the variable A to point at that new array, whereas A[:] = zip(*A[::-1]) reassigns all of the contents of A to be equal to the contents of zip(*A[::-1])

    image[:] = map(list, zip(*image[::-1]))
    return image

def cyclicFourSwap(A):
    # https://www.youtube.com/watch?v=Fxt5TkhElTA
    # 47min mark errichto solution in python.  [~i] is way nicer than [n-1-i].
    n = len(A)

    # i is the level
    for i in range(n//2):
        # j is the horizontal traversal along a level
        for j in range((n+1)//2):
            A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                        A[~j][i], A[~i][~j], A[j][~i], A[i][j]
    return A

def swap_leftright_reverse(image):
    n = len(image)
    # transpose/ swap
    for i in range(n):
        for j in range(i):
            image[i][j], image[j][i] = image[j][i], image[i][j]
    
    # left-right reverse
    for i in range(n):
        for j in range(n//2):
            image[i][j], image[i][n-j-1] = image[i][n-j-1] , image[i][j]
    return image

# 25ms. Very fast.
def rotateImage(image):
    # An nxn grid is made up of concentric hollowed out squares. I rotated these hollow concentric squares one by one by 90 degrees. 
    n = len(image[0])
    for dist in range(n//2):

        top = zip([dist]*(n - 2*dist), range(dist, n-dist))
        right = zip(range(dist + 1, n-dist), [n-dist-1]*(n-2*dist-1))
        bottom = zip([n-dist-1]*(n-2*dist-1), range(n-dist-2, dist-1, -1))
        left = zip(range(n-dist-2, dist-1, -1), [dist]*(n - 2*dist-1))

        ranges = list(top) + list(right) + list(bottom) + list(left)
        top = zip([dist]*(n - 2*dist), range(dist, n-dist))
        ranges += list(top)[1:]

        for start in range(n-2*dist-1):
            prev = start
            pr, pc = ranges[prev]
            previmage = image[pr][pc]
            while True:
                nxtind = prev + (n-2*dist-1)
                if nxtind >= len(ranges):
                    break

                nxr, nxc = ranges[nxtind]
                temp = image[nxr][nxc]
                image[nxr][nxc] = previmage

                prev = nxtind
                previmage = temp
                if ranges[start] == ranges[prev]:
                    break                
    return image


image = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

# image = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]


from copy import copy, deepcopy
# shallow copy will give error. 

print(rotateImage(deepcopy(image)))
print(topdown_reverse_swap(deepcopy(image)))
print(swap_leftright_reverse(deepcopy(image)))
print(cyclicFourSwap(deepcopy(image)))


# Deep copy is a process in which the copying process occurs recursively. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. Using shallow copy: image.copy() does not work for a 2d matrix.