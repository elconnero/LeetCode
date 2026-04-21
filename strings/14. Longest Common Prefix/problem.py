class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        result = ""
        for i in range(len(strs[0])):
            if all(i < len(word) and word[i] == strs[0][i] for word in strs):
                result += strs[0][i]
            else:
                return result
        return result
    
test = Solution()
output = test.longestCommonPrefix(["flower","flow","flight"])
print(output)