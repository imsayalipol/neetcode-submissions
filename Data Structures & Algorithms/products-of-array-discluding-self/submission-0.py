class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalList = []
        prod, zeros =1,0

        for i in nums:
            if i:            
                prod *= i
            else:
                zeros+=1
        
        if zeros>1:
            return [0]*len(nums)

        for n in nums:
            if zeros:
                if n:
                    finalList.append(0)
                else:
                    finalList.append(prod)
            else:
                finalList.append(prod//n)
        
        return finalList
                