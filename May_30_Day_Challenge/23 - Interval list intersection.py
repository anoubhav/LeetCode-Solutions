def mysoln_intervalIntersection(A, B):
    # 96% fast solution. O(M + N). 
    # Intuition: I explored the intervals with endpoints in descending order using max heap. This made the implementation simpler. 

    # Previously (below), I was using intervals with start points in ascending order in a min heap. I got incorrect answer by this technique

    # edge case
    if A == [] or B == []:
        return []

    # In the tuple, I add the key (highest end point is popped first) and the list it comes from
    all_intervals = []
    for interval in A:
        all_intervals.append([-interval[1], *interval, 'a']) # putting the key in the beginning for heap
    for interval in B:
        all_intervals.append([-interval[1], *interval, 'b'])

    import heapq

    # O(M+N) heapify is linear time
    heapq.heapify(all_intervals)


    ans = []
    prev = heapq.heappop(all_intervals)

    while all_intervals:
        curr = heapq.heappop(all_intervals)
        if curr[-1] == prev[-1]: 
            # no intersection, disjoint pairs amongst intervals in same list.
            prev = curr
            pass 
        else:
            # different list elements

            if curr[2] < prev[1]:
                # no intersection
                prev = curr
                pass

            elif curr[2] >= prev[1]:
                if prev[1] >= curr[1]:
                    ans.append([prev[1], curr[2]])
                    prev = curr
                else:# prev[1] < curr[1]
                    ans.append([curr[1], curr[2]])
                    # do not reset prev. This is the case where prev's end point is large and encompases multiple intervals from other list.

    return sorted(ans, key = lambda x: x[0])
    
def disc_page(A, B):
    # O(M + N). 
    # Intuition, intersection is guaranteed to occur IFF A.start <= B.end AND B.start <= A.end.
    # When this does not happen

    # If A[0] has the smallest endpoint, it can only intersect B[0]. After, we can discard A[0] since it cannot intersect anything else. As if it intersects both B[0] and B[1], then B[0] and B[1] won't be disjoint. And thats a contradiciton.

    # Similarly, if B[0] has the smallest endpoint, it can only intersect A[0], and we can discard B[0] after since it cannot intersect anything else.

    # We use two pointers, i and j, to virtually manage "discarding" A[0] or B[0] repeatedly.

    i = j = 0
    ans = []
    while i<len(A) and j<len(B):
        if A[i][0] <= B[j][1] and A[i][1] >= B[j][0]:
            ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
        if A[i][1] < B[j][1]:
            i+=1
        else:
            j+=1
    return ans


A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(mysoln_intervalIntersection(A, B))
print(disc_page(A,B))















############ MY FAILED IF-ELSE ATTEMPT ##################. It was failing in the case when the current interval is very large and encompasses multiples intervals in the other list. As I was resetting previous to curent every iteration.
    # if A == [] or B == []:
    #     return []
    # import heapq
    # all_intervals = []
    # for interval in A:
    #     all_intervals.append((interval[0], 's1'))
    #     all_intervals.append((interval[1], 'e1'))
        
    # for interval in B:
    #     all_intervals.append((interval[0], 's2'))
    #     all_intervals.append((interval[1], 'e2'))


    # heapq.heapify(all_intervals)
    
    # prev = heapq.heappop(all_intervals)
    # ans  = []
    # start = 0
    
    # while all_intervals:
    #     curr = heapq.heappop(all_intervals)
        
    #     # If previous and current number come from the same list (either A or B)
    #     if start:
    #         if curr[0]
    #         start = 0
    #         ans.append([prev[0], curr[0]])
        
    #     elif (prev[1] == 'e1' and curr[1] == 's2') or (prev[1] == 'e2' and curr[1] == 's1'):
    #         if prev[0] == curr[0]:
    #             ans.append([prev[0], prev[0]])
    #         else:
    #             # no intersections
    #             pass
        
    #     elif prev[1] == 's1' and curr[1] == 'e2':
    #         ans.append([prev[0], curr[0]])
    #     elif prev[1] == 's2' and curr[1] == 'e1':
    #         ans.append([prev[0], curr[0]])

    #     elif prev[1] == 's1' and curr[1] == 's2':
    #         start = 1
        
    #     elif prev[1] == 's2' and curr[1] == 's1':
    #         start = 1
        
    #     prev = curr
            
    # return ans

