class Solution:

    def getFreqString(self, word: str) -> str:
        freq = [0] * 26

        for char in word:
            freq[ord(char) - ord("a")] += 1

        frequency_string = []
        ch = "a"

        for count in freq:
            frequency_string.append(ch)
            frequency_string.append(str(count))
            ch = chr(ord(ch) + 1)

        return "".join(frequency_string)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = self.getFreqString(word)

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)

        return list(groups.values())
