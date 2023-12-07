class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in reversed(s):
            if i!=' ':
                count += 1
            elif count == 0:
                continue
            else:
              break
        return count
