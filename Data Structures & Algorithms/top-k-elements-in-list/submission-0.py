class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we put it into the hashset to find the unique numbers. Then we can run a hashmap to find how many times the number is repeating and everytime it repeats add into the map. THen which value is highest we return the output. 

        topNums = {}
        for unique in nums:
            if unique in topNums:
                topNums[unique] = topNums[unique] + 1
            else: 
                topNums[unique] = 1

        sorted_pairs = sorted(topNums.items(), key=lambda pair: pair[1], reverse=True)

        result = []
        for pair in sorted_pairs[:k]:
            result.append(pair[0])
        
        return result
