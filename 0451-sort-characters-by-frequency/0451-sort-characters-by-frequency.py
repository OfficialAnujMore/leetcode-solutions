"""
Time complexity: O(n)
Space complexity: O(n)

Test case: hollywood
Intution:
1. Start by counting char_count of each char in the given string for the given test case output will look like
{
    h:1,
    o:3,
    l:2,
    y:1,
    w:1,
    d:1,
}
2. Based on the char_count map create a new char_count map with values as follow
{
    1:[h,w,d],
    2:[l],
    3:[o]
}
3. Now from the max char_count value loop are create output array
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = {}
        result = []

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        freq_to_chars = {}
        max_freq = -1

        for key in char_count:
            value = char_count[key]
            max_freq = max(max_freq, value)
            if value not in freq_to_chars:
                freq_to_chars[value] = [key]
            else:
                freq_to_chars[value].append(key)

        for key in range(max_freq, 0, -1):
            if key in freq_to_chars:
                value = freq_to_chars[key]
                for element in value:
                    result.append(element * key)

        return "".join(result)
