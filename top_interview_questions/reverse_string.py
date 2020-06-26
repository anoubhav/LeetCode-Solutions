def reverse_string_two_pointer(s):
     # O(N) time and O(1) space.
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return s

def reverse_string_one_pointer(s):
    # O(N) time and O(1) space.
    i = 0
    while i < len(s)//2:
        s[i], s[~i] = s[~i], s[i]
        i += 1
    return s

def reverse_string_recursive(s):
    # O(N) time and O(N) space for recursive stack. In place.
    l = len(s)
    if l < 2:
        return s
    return reverse_string_recursive(s[l//2:]) + reverse_string_recursive(s[:l//2]) 

def reverse_string_pythonic(s):
     # O(N) time and O(1) space.
    s.reverse()
    return s


s = ["h","e","l","l","o"]
print(reverse_string_pythonic(s.copy()))
print(reverse_string_two_pointer(s.copy()))
print(reverse_string_one_pointer(s.copy()))
print(reverse_string_recursive(s.copy()))

# Does in-place mean constant space complexity?
# No. By definition, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure. The tricky part is that space is used by many actors, not only by data structures. The classical example is to use recursive function without any auxiliary data structures.