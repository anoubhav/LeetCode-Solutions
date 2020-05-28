def soln1(num):
    return [bin(i).count('1') for i in range(num+1)]

def soln2(num):
    ans = [0, 1, 1, 2]
    prev = [1, 2]
    totlen = 4
    while totlen<=num+1:
        new = prev + [i+1 for i in prev]
        ans += new
        totlen += 2*len(prev)
        prev = new

    return ans[:num+1]

# The logic of res[i] = res[i >> 1] + (i & 1) is that res[i >> 1] counts all bits but the least significant bit, and (i & 1) counts the least significant bit
def discpage(num):
    ans = [0]
    for i in range(1, num+1):
        ans.append(ans[i>>1] + (i&1))
    return ans

n = 12
print(soln1(12))
print(soln2(12))
print(discpage(12))
        