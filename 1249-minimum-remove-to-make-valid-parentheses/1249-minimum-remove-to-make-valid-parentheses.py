class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char == "(":
                open_stack.append(i)
            elif char == ")":
                if open_stack:
                    open_stack.pop()
                else:
                    to_remove.add(i)

        to_remove.update(open_stack)

        return "".join(char for i, char in enumerate(s) if i not in to_remove)
