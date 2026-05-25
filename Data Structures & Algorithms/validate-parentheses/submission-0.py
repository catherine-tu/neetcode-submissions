class Solution:
    def isValid(self, s: str) -> bool:
        # approach: stack for open & corresponding closed paren; guarantees correct order
        stack = []
        diction = {')': '(', '}': '{', ']': '['}

        for char in s:
            # end -- check if matching
            if char in diction:
                if stack and stack[-1] == diction[char]:
                    stack.pop()
                else: 
                    return False
            # otherwise, its an opening -- 
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False
            

