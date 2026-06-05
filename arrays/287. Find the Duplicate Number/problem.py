class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = {}

        for n in nums:
            if n in seen: 
                seen[n] += 1
                if seen[n] == 2: return n

            else: seen[n] = 1

sol = Solution()

testcase_array = [
    [1,3,4,2,2],
    [3,1,3,4,2],
    [3,3,3,3,3]
]

for i in range(len(testcase_array)): print(sol.findDuplicate(testcase_array[i]))