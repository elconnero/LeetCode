class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = [0] * k
        table = {}

        for element in nums:
            if element in table: table[element] += 1
            else: table[element] = 1

        for i in range(1, k+1): res[i-1] = sorted(table, key=table.get, reverse=True)[i - 1]

        return res
    

test = Solution()
testcase_nums = [[1,1,1,2,2,3], [1,2,1,2,1,2,3,1,3,2], [1]]
testcase_k = [2, 2, 1]
for i in range(len(testcase_nums)):
    prints = test.topKFrequent(testcase_nums[i], testcase_k[i])
    print(prints)
    