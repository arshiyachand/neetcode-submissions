class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputprod = math.prod(nums)
        outputlist = []

        for i in range(len(nums)):
            if nums[i] == 0:
                tempprod = math.prod(nums[:i]) * math.prod(nums[i+1:])
                outputlist.append(tempprod)
            else:
                outputlist.append(outputprod//nums[i])
        return outputlist

        