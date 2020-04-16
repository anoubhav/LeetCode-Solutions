# Approach 1: Performing all shifts
def all_shifts(s, shift):
    for row in shift:
        direction, amt = row

        if direction == 0:
            s = s[amt:] + s[:amt]
        else:
            s = s[-amt:] + s[:-amt]
    print(s)

# Approach 2: Performing NET shift
def single_shift(s, shift):
    net = 0
    for row in shift:
        direction, amt = row
        if direction:
            net += amt
        else:
            net -= amt
    # Incase the net shift is a mulitple of length of string
    direction = 1 if net>0 else 0
    amt = abs(net)%(len(s))

    if direction == 0:
        s = s[amt:] + s[:amt]
    else:
        s = s[-amt:] + s[:-amt]
    print(s)

if __name__ == '__main__':
    s = "abcdefg"
    shift = [[1,1],[1,1],[0,2],[1,3]]

    # Approach 1
    all_shifts(s, shift)

    # Approach 2
    single_shift(s, shift)







