class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #outputDict = Counter(nums)
       # return True if any(value > 1 for value in outputDict.values()) else False

        seen = set()

        for i in nums:
            if i in seen:
                return True

            seen.add(i)
        return False