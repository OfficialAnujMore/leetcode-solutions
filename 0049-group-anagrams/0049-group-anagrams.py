"""
Time complexity: O(n * k log k), where n is the number of strings and k is the maximum string length.

Space complexity: O(n * k) for storing the grouped strings and keys.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}
        result = []
        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str not in freq:
                freq[sorted_str] = [word]
            else:
                freq[sorted_str].append(word)

        for key in freq:
            result.append(freq[key])
        return result
