# Trial 1
# class NumArray(object):

#     def __init__(self, nums):
        
#         self.pre_array = [0] * len(nums)
#         for i in range(len(nums)):
#            self.pre_array[i] += nums[i-1]

        

#     def sumRange(self, left, right):
        
#         return self.pre_array[right] - self.pre_array[left]
    
# Trial 2 - Works
# class NumArray(object):

#     def __init__(self, nums):
        
#         self.pre_array = nums[:]
        

        

#     def sumRange(self, left, right):

#         ans = 0
#         for i in range(left, right+1):

#             #print("i=",i)
#             #print("prearray =",self.pre_array[i])
#             ans = ans + self.pre_array[i]
           
        
#         return ans
    
# Trial 3

class NumArray(object):

    def __init__(self, nums):
        
        self.pre_arr = [0]
        for num in nums:
            self.pre_arr.append(self.pre_arr[-1] + num)
        
    def sumRange(self, left, right): return self.pre_arr[right+1] - self.pre_arr[left]
    


    

    
test = NumArray([-2, 0, 3, -5, 2, -1])

work = test.sumRange(0,5)
print(work)