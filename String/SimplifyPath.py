'''
https://leetcode.com/problems/simplify-path/
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur_folder = ''
        for ch in path+'/':
            if ch == '/':
                if cur_folder == '..':
                    if stack: stack.pop()
                elif cur_folder != "" and cur_folder != ".":
                    stack.append(cur_folder)
                cur_folder = ""
            else:
                cur_folder += ch
        return "/" + "/".join(stack)