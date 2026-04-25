class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempList = []
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


strs = ["act","pots","tops","cat","stop","hat"]
g = Solution()
g.groupAnagrams(strs) 