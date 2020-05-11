def mysoln_findJudge(N, trust) -> int:
    # edge case 
    if trust == []:
        if N == 1:
            return 1
        else:
            return -1
    
    # dictionary/hash map of untrustworthy people
    untrust_freq = dict()
    
    # Set of trustworthy people (i) *occured* earlier
    occured = set()
    
    for i, j in trust:
        occured.add(i)
        
        # if i (trusts) in untrust then delete; O(1) look up; 
        if i in untrust_freq:
            del untrust_freq[i]
        
        # if j (not trusts) not present in previously occured trustworthy people then get frequency
        if j not in occured:
            untrust_freq[j] = untrust_freq.get(j, 0) + 1
    
    # How many untrustworthy remain?
    if len(untrust_freq.keys()) == 0:  return -1 # the set of people who trust nobody
    
    else:
        for k, v in untrust_freq.items():
            # there can only one person, who is trusted by everybody, i.e, his frequency is N-1
            if v == N - 1:
                return k
    return -1

def discpage(N, trust):

    if N == 1:
        return 1
    
    trust_scores = [0]*(N+1)

    for i, j in trust:
        trust_scores[i] -= 1
        trust_scores[j] += 1
    
    for person in range(1, N+1):
        # The town judge trusts nobody. Everybody (except for the town judge) trusts the town judge.
        if trust_scores[person] == N-1:
            return person

    return -1