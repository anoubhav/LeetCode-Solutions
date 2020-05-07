def single_pass(s):
    # Maxscore = max(zeroL + one R)
    # Maxscore = max(zeroL - oneL + oneR + oneL)
    # Maxscore = max(zeroL - oneL) + total_one (constant)

    zero, one, score = 0, 0, -1 # in case of all ones, -1 is needed as corner case.
    for i, char in enumerate(s):
        if char == '0': zero += 1
        else: one += 1
        if i!= len(s) - 1: # to prevent empty substring
            score = max(score, zero - one)
    
    return score + one


def my_soln(s):
    #  Count prefix zeros p0 and suffix ones s1, then answer = max p0[i] + s1[i] for i in [1, n)
    lzero = []
    rone = []
    
    totzero, totone = 0, 0
    
    for num in s:
        t = int(num)
        if t == 0:
            totzero +=1
        else:
            totone += 1
        
        # number of zeros till index i
        lzero.append(totzero)
        # number of ones till index i
        rone.append(totone)
        
    # number of ones after index i
    rone = [totone - i for i in rone]
    score = 0
    
    # -1 is used to prevent empty right substring split
    for a, b in zip(lzero[:-1], rone[:-1]):
        if a+b>score:
            score = a+b

    return score

print(my_soln('010101111'))
print(single_pass('010101111'))
print(single_pass('1111'))