class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexdict = {}
        for i,n in enumerate(numbers):
            indexdict[n] = i

        for i,n in enumerate(numbers):
            diff = target - n
            if diff in indexdict and indexdict[diff] != i:
                return [i+1,indexdict[diff]+1]
        return []
        