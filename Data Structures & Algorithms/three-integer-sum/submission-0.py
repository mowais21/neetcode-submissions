class Solution:
    # Return all triplets where the sum is 0. 
    # Constraint: The indices i,j,k are all distinct. 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array, and pick a number. Use a 2 pointer approach to find the target

        nums.sort() # nlog(n)

        res = []

        for i in range(len(nums)):
            target = -nums[i]

            j = i + 1
            k = len(nums) - 1

            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                current = nums[j] + nums[k]

                if current > target:
                    k -= 1
                elif current < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1

                    # skip duplicates for j
                    while nums[j] == nums[j-1] and j < k:
                        j += 1


        return res