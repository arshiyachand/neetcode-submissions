class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        output = "".join([char for char in s if char.isalnum()])
         
              
        output = output.lower()
        print(output[::-1])

        return True if output == output[::-1] else False
        