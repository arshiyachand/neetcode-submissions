class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encodedstring = ""
        for i in strs:
            encodedstring = encodedstring+str(len(i))
            encodedstring = encodedstring+"*"
            encodedstring = encodedstring+i
        print(encodedstring)
        return encodedstring

    def decode(self, s: str) -> List[str]:
        i = 0
        
        decodedList = []

        while i < len(s):
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            if j < len(s) and s[j] == "*":          
                lenStr = int(s[i:j])
                start = j+1
                end = start+lenStr
                decodedList.append(s[start:end])
                i = end
            else:
                i+= 1
        
        return decodedList




        
