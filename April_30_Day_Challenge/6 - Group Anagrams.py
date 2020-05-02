# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/

# Given an array of strings, group anagrams together.
## Canonical Form type problems

from collections import defaultdict

def by_sorted_string(strs):
    # Two strings are anagrams if and only if their sorted strings are equal. Time complexity: O(N*KlogK), where N is the number of strings and K is the maximum length of a string in strs. Space complexity: O(N*K)

    d = {}
    for str in strs:
        d[tuple(sorted(str))] = d.get(tuple(sorted(str)), []) + [str]
    
    return list(d.values())

def get_count_tuple(string):
    lst = [0]*26
    for char in string:
        lst[ord(char) - ord('a')] += 1
    return tuple(lst)

def by_character_count(strs):
    # Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same. Time complexity: O(N*K) and space complexity: O(N*K)
    
    d = defaultdict(list)
    for string in strs:
        d[get_count_tuple(string)].append(string)
    return list(d.values())


def groupAnagrams(strs):

    # return by_sorted_string(strs)
    return by_character_count(strs)
    

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))