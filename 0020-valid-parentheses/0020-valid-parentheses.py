class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_char = ["(", "[","{"]
        close_char = [")", "]","}"]

        for i in s:
            if i in open_char:
                stack.append(i)
            else:
                if stack and stack.pop() == open_char[close_char.index(i)]:
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False