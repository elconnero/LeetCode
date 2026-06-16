def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]  # start with the empty subset

    for num in nums:
        new_subsets = [curr + [num] for curr in result]
        result += new_subsets

    return result

print(subsets([1, 2, 3]))
# [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]