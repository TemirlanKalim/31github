class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim leading and trailing spaces
        s = s.strip()
        
        # Step 2: Split the string into a list of words
        words = s.split()
        
        # Step 3: Reverse the list of words
        words.reverse()
        
        # Step 4: Join the reversed list into a string
        result = ' '.join(words)
        
        return result
