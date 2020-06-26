def reverse_integer(x):
    isneg = x<0
    x = abs(x)
    revx = 0
    while x > 0:
        revx = revx*10 + x%10
        if revx > 2**31 - 1:
            return 0
        x //= 10
    return revx*(-1 if isneg else 1)