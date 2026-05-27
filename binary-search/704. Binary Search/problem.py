class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return -1
    
testcases_arr = [[-1,0,3,5,9,12], [-1,0,3,5,9,12]]
testcases_target = [9,2]

practice = Solution()

for i in range(len(testcases_arr)):
    print(practice.search(testcases_arr[i], testcases_target[i]))