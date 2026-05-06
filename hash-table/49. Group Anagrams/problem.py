class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for element in strs:
            count = [0] * 26
            for char in element:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(element)

        return list(res.values())