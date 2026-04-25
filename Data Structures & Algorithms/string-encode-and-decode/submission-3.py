class Solution:
    def encode(self, l:list[str])->str:
        encStr=""
        for s in l:
            encStr += str(len(s)) + "#" +  "".join(s)
        return encStr
                
    def decode(self, strs:str)->list[str]:
        start = 0
        decodeStr = []
        
        while start < len(strs):
            end=start

            while strs[end] != "#":
                end += 1
            length = int(strs[start:end])
            start = end+1
            end = start+length

            decodeStr.append(strs[start:end])
            start=end            

        return decodeStr
                
            
s = Solution()
encStr = s.encode(["we","say",":","yes","!@#$%^&*()"])

decode = s.decode(encStr)
