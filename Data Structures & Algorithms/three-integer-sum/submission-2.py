class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        res = set()
        numbers.sort()
        

        for i, n in enumerate(numbers):
            if n > 0:
                break
            
           
            l = i+1
            r = len(numbers) - 1
            while l < r:
                curr = numbers[l] + numbers[r] + n
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.add((n,numbers[l],numbers[r]))
                    l += 1
                    r -= 1
                    

        return [list(i) for i in res]
         