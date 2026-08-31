from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # try again
        # hash map: track frequencies of each 
        maps = defaultdict(int)
        for char in s:
            maps[char] += 1
        
        for char in t:
            if char not in maps:
                return False
            maps[char] -= 1

        for val in maps.values():
            if val != 0:
                return False
        
        return True

        
        
        

        # # approach: loop through each letter, and if it's a match, remove from t
        # for char in s:
        #     if char in t: 
        #         t = t.replace(char, '', 1) # only remove 1
        #     else:
        #         return False
        
        # return t == ''