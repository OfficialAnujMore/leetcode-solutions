"""
Intution

s = "abcabcbb"

Possible ["abc", "bca", "cab", "abc",bc, cb]

s = "bbbbb"

Possible output = ["b"]
     012345
s = "pwwkewz"

Possible output = [p, pw, w, wk, wke, kew, kewz]
     0123456789
s = "es $ , ## xyzwwabc .."

Possible output = ["es $ , #", "# xyzw" , "wabc .", "." ]


Algoritm

l = 0
r = l+1
result = 0
myset = [s[l]]
while r < len(str):
    if s[r] in myset:
        while s[r] not in myset:
            l+=1
    myset.append(s[r])
    result = max(result, r-l)

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if n <= 1:
            return n

        left = 0
        right = left + 1
        myset = []
        myset.append(s[left])
        result = 0

        while right < n:
            # print(f"Myset: {myset}, {left}, {right}")
            # if s[right] in myset:
            while s[right] in myset:
                # Remove the left most value from the set
                myset.remove(s[left])
                left += 1
            myset.append(s[right])
            result = max(result, right - left+1)
            right += 1

        return result
