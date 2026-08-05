class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedList = []
        for word in strs:
            encodedList.append(str(len(word)) + "#" + word)
        return "".join(encodedList)














    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0
        while i < len(s):
            index = s.find("#", i)
            length = int(s[i:index])
            decodedList.append(s[index +1: index + 1 + length]) 
            i = index + 1 + length
        return decodedList