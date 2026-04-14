class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need, left = 0,len(countT),0
        res, resLen = [-1,-1], float("infinity")
        
        for right in range(len(s)):

            character = s[right]
            window[character] = 1 + window.get(character, 0)

            if character in countT and countT[character] == window[character]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                #Popping element from left window
                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        left, right = res
        return s[left:right+1] if resLen != float("infinity") else ""

test = Solution()

output = test.minWindow("ADOBECODEBANC", "ABC")
print(output)
        