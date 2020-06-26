def plusOne(digits):
    n = len(digits)
    carry = 0
    for i in range(n-1, -1, -1):
        s = digits[i] + 1
        carry = 1 if s>9 else 0
        digits[i] = s%10
        if carry == 0:
            break
    if carry:
        digits = [1] + digits
    return digits

print(plusOne([2, 3, 9]))
print(plusOne([9, 9, 9]))
print(plusOne([9, 9, 4]))