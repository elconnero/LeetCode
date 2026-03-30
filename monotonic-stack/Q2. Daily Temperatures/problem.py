# ---- ATTEMPT ONE ----
# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#
#         ans = []
#         for i in range(len(temperatures)):
#             count = 1
#             print("Level 1")
#             if i <= len(temperatures):
#                 for j in range(len(temperatures)):
#                     if (i < j) and (temperatures[i] < temperatures[j]):
#                         ans.append(count)
#                         print(f"Level 2 and j={j}, i={i} and count={count} | BREAK!")
#                         break
#                     elif (i <= j) and (temperatures[i] > temperatures[j]):
#                         count += 1
#                         print(f"Level 3 j={j} , i={i}")
#                     else:
#                         continue
#                 else:
#                     ans.append(0)
#                     print(f"Level 4 i={i} and we have a 0")
#         return ans

# ---- ATTEMPT TWO ----
# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#
#         ans = []
#         for i in range(len(temperatures)):
#             print("Level 1")
#             if i <= len(temperatures):
#                 for j in range(len(temperatures)):
#                     if (i < j) and (temperatures[i] < temperatures[j]):
#                         ans.append(j - i)  # CHANGE: replaced count with j - i
#                         print(f"Level 2 and j={j}, i={i} and j-i={j-i} | BREAK!")
#                         break
#                     else:
#                         continue
#                 else:
#                     ans.append(0)
#                     print(f"Level 4 i={i} and we have a 0")
#         return ans

# ---- ATTEMPT THREE ----
class Solution(object):
    def dailyTemperatures(self, temperatures):

        ans = []
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):  # CHANGE: start j at i+1, removes need for i < j check and the wasted iterations before i
                if temperatures[i] < temperatures[j]:
                    ans.append(j - i)
                    break
            else:
                ans.append(0)
        return ans


temp = Solution()
prices = [73,74,75,71,69,72,76,73]
printME= temp.dailyTemperatures(prices)
print(printME)
