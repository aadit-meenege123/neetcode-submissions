class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for word in strs:
            printed = sorted(word)
            finalWord = "".join(printed)
            anagramMap.setdefault(finalWord, []).append(word)
        
        return list(anagramMap.values())