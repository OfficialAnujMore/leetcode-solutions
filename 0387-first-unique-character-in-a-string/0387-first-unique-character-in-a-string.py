class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i in range(len(s)):
            char = s[i]
            if freq[char] == 1:
                return i
        return -1
