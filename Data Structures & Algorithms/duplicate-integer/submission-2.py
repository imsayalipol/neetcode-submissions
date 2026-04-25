class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:            
                return True
        else:
            return False
        