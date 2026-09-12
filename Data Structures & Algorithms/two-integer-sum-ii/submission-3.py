class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        outputdict = defaultdict(int)
        for i,n in enumerate(numbers):
            outputdict[n] = i

        print(outputdict)

        for i, n in enumerate(numbers):
            if target - n in outputdict and outputdict[target-n] != i:
                return [i+1, outputdict[target-n]+1]
        