class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]

        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        
        while k>0:
            maxNum= max(d, key=d.get)
            l.append(maxNum)
            del d[maxNum]
            k-=1

        return l
        