def my_soln(s, k):
    d = set()
    for ind, i in enumerate(s):
        if ind+k<=len(s):
            w = s[ind:ind+k]
            d.add(w)
            
        else:
            break
    
    return len(d)==2**k
    # if len(d)!=2**k:
    #     return False
    # else:
    #     return True