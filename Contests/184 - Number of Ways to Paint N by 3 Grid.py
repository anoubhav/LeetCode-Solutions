# Good problem. I didn't get it on the first time. I read a similar (not same) problem of # of ways to paint Nx3 using **4 colours**
# during the 1.5 hour time and understood it and implemented the solution for the current problem.
# Src: https://www.geeksforgeeks.org/ways-color-3n-board-using-4-colors/

def numOfWays(n):
    A = [6] + [0]*(n-1)
    B = [6] + [0]*(n-1)
    
    for i in range(n-1):
        A[i+1] = 2*A[i] + 2*B[i]
        B[i+1] = 2*A[i] + 3*B[i]
    
    return (A[-1] + B[-1])%(10**9 + 7)

print(numOfWays(7))