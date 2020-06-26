# Copied from: https://leetcode.com/problems/string-to-integer-atoi/discuss/4673/60ms-python-solution-OJ-says-this-beats-100-python-submissions

# Errichto lightning fast edge case detection + code (1hr  mark) https://www.youtube.com/watch?v=Fxt5TkhElTA

def atoi(s):
    if len(s) == 0 : return 0
    ls = list(s.strip())

    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-','+'] : del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit() :
                # A faster way to do int conversion; ord('9') - ord('0') instead of int('9')
        ret = ret*10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2**31, min(sign * ret,2**31-1))