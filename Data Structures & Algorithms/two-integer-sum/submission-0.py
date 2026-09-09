class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexdict = {}
        for i,n in enumerate(nums):
            indexdict[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in indexdict and indexdict[diff] != i:
                return [i,indexdict[diff]]
        return []
        