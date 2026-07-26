class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        topNums = {}
        for unique in nums:
            topNums[unique] = 1 + topNums.get(unique,0)

        sorted_pairs = sorted(topNums.items(), key=lambda pair: pair[1], reverse=True)

        result = []
        for pair in sorted_pairs[:k]:
            result.append(pair[0])
        
        return result
