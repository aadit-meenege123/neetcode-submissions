class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topKMap = {}
        for num in nums:
            topKMap[num] = topKMap.get(num,0) + 1

        sortedList = sorted(topKMap.items(), key=lambda x:x[1], reverse=True)

        finalFrequentInt = []

        for pair in sortedList[:k] :
            finalFrequentInt.append(pair[0]) 

        return finalFrequentInt