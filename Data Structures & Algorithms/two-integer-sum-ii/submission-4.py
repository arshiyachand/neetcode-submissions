class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            curr = numbers[r] + numbers[l] 
            if curr > target:
                r = r-1
            if curr < target:
                l = l+1
            if curr == target:
                return [l+1, r+1]
        
        