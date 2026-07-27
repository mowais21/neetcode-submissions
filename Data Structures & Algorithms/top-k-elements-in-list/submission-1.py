class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Need to figure out the frequency of each element
        # 2. Need to sort elements by decreasing frequency

        # Sort the array list, frequency for all elements comes together. Store these frequencies
        # Going from frequency to frequency, fetch k elements with the highest frequencies
        
        # O(nlog(n))
        nums.sort()

        # char -> freq
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # freq -> [chars]
        # A char can have a max freq of the length of the array
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res