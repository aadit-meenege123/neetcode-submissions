class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we will solve 2 ways

        #one is the traditional 2 pointers
        # other way is we can put the string and reverse it simply check but make sure you are able to remove the spaces and uncessary stuff we can use the function isalnum()

     
        finalString = ""
        for space in s:
            if space.isalnum():
                finalString = finalString + space.lower()

        return finalString == finalString[::-1]