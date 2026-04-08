class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        last = len(numbers) - 1

        while start < last:

            if numbers[start] + numbers [last] == target: return start+1, last+2
            elif numbers[start] + numbers [last] > target: last -= 1 
            elif numbers[start] + numbers [last] < target: start += 1
            else: break
        return 0
    
test = Solution()
output = test.twoSum([2,7,11,15],9)
print(output)