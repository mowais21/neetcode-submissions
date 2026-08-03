class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums: array of integers
        # goal: find the longest consecutive sequence of elements that can be formed
        # consecutive seq: seq of elements where each element is exactly 1 greater than the previous element

        # [2,20,4,10,3,4,5]
        # [2,3,4,5], [10], [20]

        # to find the longest subsequence, we need to keep track of length of each subsequences, build on them to find bigger subsequences

        # naive solution:
        # 1. For each element in the array, start a search and find if the next element exists. O(n^2)

        # better:
        # 1. sort the array. O(nlogn)
        

        # optimization:
        # 2. maintain a set which tells if an element exists in the array
        #    sol[x] = length of biggest subsequence which starts at the string
        #    sol[x] = 1 + sol[x+1]


        elements = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in elements:
                # start of a new sequence, create a biggest run
                cur_length = 1

                while num + cur_length in elements:
                    cur_length += 1
                longest = max(longest, cur_length) 
        return longest


