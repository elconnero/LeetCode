
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):

            lo, hi = i+1, n-1
            while lo < hi:
                
                current_sum = nums[i] + nums[lo] + nums[hi]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum == target: return current_sum
                elif current_sum < target: lo += 1
                else: hi -= 1

        return closest_sum
