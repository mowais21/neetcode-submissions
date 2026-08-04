class Solution:
    # numbers: array of integers sorted in a non-decreasing order (can be repetitions of the same number)
    # 
    # returns: a pair of indices [i1, i2] such that nums[i1] + nums[i2] = target
    #          i1 != i2
    # note: indices start from 1 (not 0)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]

            if current < target:
                l += 1
            elif current > target:
                r -= 1
            else:
                return [l + 1, r + 1]


        