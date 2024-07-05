'''
https://leetcode.com/problems/minimum-window-substring/
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case
        if t == '': return ''
        # Hash maps to preserve window and target counts
        window, countT = {}, {}
        for ch in t: # Initialize count of each char from t string
            countT[ch] = 1 + countT.get(ch, 0)
        # Recording total values to avoid comparing each counts everytime
        have, need = 0, len(countT)
        # Initialize result with opposite extreme values
        res, resL = [-1, -1], float('infinity')
        # Left pointer
        l = 0
        # Right pointer
        for r in range(len(s)):
            ch = s[r]
            # Adding all chars with count to the window
            window[ch] = 1 + window.get(ch, 0)
            # Only add chars count to `have` if a ch in `need`` and
            # if ch count in current windows equals to its equalent ch in countT
            if ch in countT and window[ch] == countT[ch]:
                have += 1
            # Reduce window size from left when we meet condition for min substring
            while have == need:
                # Update result
                cur_win_size = r - l + 1
                if cur_win_size < resL:
                    res = [l, r]
                    resL = cur_win_size
                # remove left ch count in window and window size
                window[s[l]] -= 1
                # only reduce count from have if left ch in need
                # out of balance to it equivalent ch in countT
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resL != float('infinity') else ''
