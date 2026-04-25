class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
                if d[nums[i]]>1:
                    return True
        else:
            return False
        