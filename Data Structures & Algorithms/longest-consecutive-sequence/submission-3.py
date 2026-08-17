class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        #removing duplicates
        longest = 0
        for num in num_set:
            if num-1 not in num_set:
                length = 1
            #nothing else in the set return as 1
                while num + length in num_set:
                    length +=1
                    #if something in the set then return length + 1
                longest = max(longest,length) 

        return longest
