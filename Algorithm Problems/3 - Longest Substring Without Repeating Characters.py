def mysoln_lengthOfLongestSubstring(s: str) -> int:
    # O(n+n) solution. outer for loop scans array, inner for loop checks if substring unique ;start pointer does not reset
    # for each outer loop iteration. Thus, it is NOT O(n*n), instead O(n+n)
    # naive solution would iterate over all substrings and then check if substring unique = O(n*n*n)

    # set stores the characters encountered in current substring
    charset = set()
    # starting index of substring
    start = 0

    ans = 0
    msf = 0 # max len so far
    for i, end in enumerate(s):
        # character encountered earlier; move start pointer ahead - O(N)
        if end in charset:
            for ch in range(start, i):
                if s[ch] == end:
                    break
                charset.remove(s[ch])
                
            msf = i - ch
            start = ch + 1

        # new
        else:
            msf += 1
            charset.add(end)

        if msf>ans: ans = msf

    return (ans)

def best_lengthOfLongestSubstring(s: str) -> int:
    # The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.

    d = {}
    ans, msf = 0, 0
    start = 0

    for i, char in enumerate(s):
        if char in d:
            temp = d[char] + 1
            if temp > start:
                start = temp
                
        d[char] = i # index of the latest position of character
        msf = i - start + 1 # lenght of substring
        if msf>ans: ans = msf

    return ans

