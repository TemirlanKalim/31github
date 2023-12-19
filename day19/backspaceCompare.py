class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s, new_t = [], []
        for i in s:
            if i == '#':
                if len(new_s)!= 0:
                    new_s.pop()
            else:
                new_s.append(i)
        for j in t:
            if j == '#':
                if len(new_t)!= 0:
                    new_t.pop()
            else:
                new_t.append(j)
        print(new_s, new_t)
        return new_s == new_t
        
