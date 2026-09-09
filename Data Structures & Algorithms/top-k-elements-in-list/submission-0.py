class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        outputDict = Counter(nums)
        top_k = outputDict.most_common(k)

        print(top_k)
        return [num for num, freq in top_k]

        