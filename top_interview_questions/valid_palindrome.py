def isPalindrome(s):
    import string
    snew = ''
    for i in s:
        # check for alphanumeric characters in string; discard rest
        if i in string.ascii_letters or i in string.digits:
        # if i.isalnum():
            snew += i.lower()

    return snew == snew[::-1]
    # n = len(snew)
    # i = 0

    # while i < n//2:
    #     if snew[i] == snew[n-i-1]:
    #         pass
    #     else:
    #         return False
    #     i += 1
    # return True

s = "A man, a plan, a canal: Panama"
s = "abbʼa" #is_alnum fails on this. replaced it with ascii_letters and ascii_digits.
print(isPalindrome(s))