import math
def findComplement(self, num: int) -> int:
    # soln 1
    b = bin(num)[2:]
    ans = ''
    for i in b:
        ans += ('0' if i == '1' else '1')
    # return int(ans, 2)
    
    # soln 2
    ans = ''
    while num>0:
        ans += str(1 - (num & 1))
        num >>= 1
    # return int(ans[::-1], 2)
    
    # soln 3
    digits = math.floor(math.log2(num)) + 1
    mask = (1<<digits) - 1
    # return mask ^ num

    ## soln 4
    mask =  '1' * num.bit_length()
    # return num ^ int(mask , 2)