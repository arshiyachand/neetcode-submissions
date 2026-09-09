class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        
        left = 0
        right = len(s1)-1
        output = False

        while right < len(s2):
            if self.ispermutation(s1, s2[left:right+1]):
                output = True
            left += 1
            right += 1

        return output
            


    def ispermutation(self,s1, s2):
        l1 = Counter(s1)
        l2 = Counter(s2)
        if l1 == l2:
            return True
        else:
            return False