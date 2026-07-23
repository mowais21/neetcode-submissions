class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Need to group the strings. Each anagram goes to its own group.
        # Each string can only go to 1 group
        # 1. Use a freqMap
        # 2. Anything better? Some sort of hash?

        groupByFreqMap = {}

        for word in strs:
            hashWord = ''.join(sorted(word))
            if hashWord not in groupByFreqMap:
                groupByFreqMap[hashWord] = [word]
            else:
                groupByFreqMap[hashWord].append(word)

        return [groupByFreqMap[k] for k in groupByFreqMap]
