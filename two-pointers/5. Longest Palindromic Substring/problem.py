# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         res = ""
#         storage = []

#         front, end  = 0, len(s)-1

#         for i in range(len(s)):
#             if s[front] == s[end]:
#                 res += s[front]
#                 front += 1
#                 end -= 1
#             else:
#                 storage.append(res)
#                 res = ""
#                 front += 1
#                 end -= 1
#         return max(storage, key=len)
            
# test = Solution()
# output = test.longestPalindrome("abcbaxyz") #This failed my version
# print(output)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s[::-1] == s: return s
        
        storage = []

        for i in range(len(s)):
            for j in range(len(s)-1,-1,-1):
                if s[i] == s[j]:
                    window = s[i:j+1]
                    if window == window[::-1]:
                        storage.append(window)
        return max(storage, key=len)


            
test = Solution()
testcase = ["abcbaxyz","babad", "cbbd", "jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"]
for i in range(len(testcase)):
    output = test.longestPalindrome(testcase[i]) #This failed my version
    print(output)


#This was the fast way
"""
class Solution(object):
    def longestPalindrome(self, s):
        if s[::-1] == s:
            return s
        
        # inti start at 0 and window size is 1
        odStart, odsize = 0, 1
        
        #checking odd length
        for i in range(2, len(s)):
            l = i - odsize - 1
            if (l < 0):
                continue
            r = i + 1
            s1 = s[l : r]
            if (s1 == s1[::-1]):
                odStart = l
                odsize = odsize + 2
        
        evSize = odsize - 1 # any even lenth should be greater than this
        evStart = 0

        # checking for even lengths
        for i in range(1 + evSize, len(s)):
            l = i - evSize - 1
            r = i + 1

            if (l < 0):
                continue

            s1 = s[l : r]
            if (s1 == s1[::-1]):
                evStart = l
                evSize += 2

        if (evSize > odsize):
            return s[evStart:evStart+evSize]
        return s[odStart:odStart+odsize]
"""
