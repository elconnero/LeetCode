class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        ans = []

        if k == 0: return len(code) * [0]
        elif k > 0:
            for element in range(len(code)):
                element_sum = 0
                for k_index in range(1, k+1):

                    # if element + k_index <= len(code) - 1: element_sum += code[element + k_index]
                    # else: element_sum += code[(len(code)-1) - k_index]
                    if element + k_index <= len(code) - 1:  element_sum += code[element + k_index]
                    else:  element_sum += code[element + k_index - len(code)]
                ans.append(element_sum)
            return ans
        else:
            for element in range(len(code)):
                element_sum = 0
                for k_index in range(1, abs(k) + 1):

                    if element - k_index >= 0: element_sum += code[element - k_index]
                    else: element_sum += code[element - k_index + len(code)]
                ans.append(element_sum)
            return ans

sol = Solution()

test_cases = [
    ([5, 7, 1, 4], 3),    # [12, 10, 16, 13]
    ([1, 2, 3, 4], 0),    # [0, 0, 0, 0]
    ([2, 4, 9, 3], -2),   # [12, 5, 6, 13]
    ([1], 0),              # [0]
    ([1, 2], 1),            # [2, 1]
    ([1, 2, 3], -1),       # [3, 1, 2]
    ([5, 5, 5, 5], 2),     # [10, 10, 10, 10]
]

for code, k in test_cases:
    output = sol.decrypt(code, k)
    print(output, " ", k, " ", code)


