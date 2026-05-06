class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        
        table1 = {}
        for char in s:
            if char in table1:
                table1[char] += 1
            else:
                table1[char] = 1

        for char in t:
            if char not in table1: return False
            table1[char] -= 1
            if table1[char] < 0: return False
        return True