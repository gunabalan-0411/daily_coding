class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch == '#' and s_stack:
                s_stack.pop()
            elif ch != '#':
                s_stack.append(ch)
        for j in range(len(t)):
            ch = t[j]
            if ch == '#' and t_stack:
                t_stack.pop()
            elif ch != '#':
                t_stack.append(ch)
        print(s_stack, t_stack)
        return ''.join(s_stack) == ''.join(t_stack)
        