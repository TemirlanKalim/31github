class Solution:
    def isValid(self, s: str) -> bool:
        kek = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                kek.append(i)
            elif i == ')':
                if not kek or kek.pop() != '(':
                    return False
            elif i == '}':
                if not kek or kek.pop() != '{':
                    return False
            elif i == ']':
                if not kek or kek.pop() != '[':
                    return False
            else:
                return False
        if not kek:
            return True
        return False
