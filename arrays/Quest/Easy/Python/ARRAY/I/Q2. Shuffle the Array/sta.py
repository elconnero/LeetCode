class Solution(object):
    def shuffle(self, nums, n):
        
        array1 = nums[:n]
        array2 = nums[n:]
        shuffled_array = []
        for i in range(min(len(array1), len(array2))):
            shuffled_array.append(array1[i])
            shuffled_array.append(array2[i])
        return shuffled_array
        
Check = Solution()

nums = [0,1,2,3,4,5,6,7,8]
n = len(nums)/2
answer = Check.shuffle(nums, n)
print(answer)
