# Solved - 5:30 mins

def my_soln(target, n):
    # O(n*max(target))
    ans = []
    for i in range(1, n+1):
        
        if target[-1] < i:
            break

        ans.append('Push')
            
        if i not in target:
            ans.append('Pop')
            
    return ans

def alternate(target, n):
    # O(max(target))
    c = 0
    ans = []
                        # max element in target
    for i in range(1, target[-1] + 1):
        ans.append('Push')
        if target[c] == i:
            c += 1
        else:
            ans.append('Pop')
    
    return ans