class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       indices={}
       for i, n in enumerate(nums):
            indices[n]=i
       
       for x in range(0,len(nums)):
            t = target-nums[x]

            if t in indices and indices[t]!=x:
                return [x, indices[t]]
