class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return None
        s=s.lower()
        s=re.sub(r'[^a-zA-Z0-9]',"", s)
        
        reverseS = s[::-1]

        print(reverseS)

        if s == reverseS:
            return True
        return False
        