class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        d= {}

        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
                        
        while k>0:
            max_key = max(d, key=d.get)

            l.append(max_key)
            del(d[max_key])
            
            k-=1

        return l       