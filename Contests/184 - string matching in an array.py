# Solution used in contest. Time complexity: O(N^2*K), where N is the length of input word array and K is length of longest word.
# Naive solution
def stringMatching(words):
    ans = []
    n = len(words)
    for i in range(n):
        for j in range(n):
            if words[i] in words[j] and i!=j:
                ans.append(words[i])
                break
    
    return ans

print(stringMatching(words = ["leetcode","et","code"]))