class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        if len(s2) < len(s1):
            return False
        l = 0 
        r = len(s1) 
        curr = ""
        sorteds1 = "".join(sorted(s1))
        while r < len(s2)+1:
            curr = s2[l:r]
            curr = "".join(sorted(curr))
            print(curr)
            if curr == sorteds1:
                return True
            l += 1
            r += 1

        return False


            

   
        