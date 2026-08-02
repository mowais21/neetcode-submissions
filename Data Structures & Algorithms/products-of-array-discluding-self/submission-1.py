class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2 phase
        # 1. One array maintains product of all elements to the left (excluding current)
        # 2. One array maintains product of all elements to the right (excluding current)

        # [1,2,4,6]
        # leftProduct = [1,1,2,8]
        leftTotal = 1
        leftProduct = [1 for i in range(len(nums))]
        for i in range(1, len(nums), 1):
                leftTotal *= nums[i-1]
                leftProduct[i] = leftTotal

        # print(leftProduct)

        # [1,2,4,6]
        # rightProduct = [48,24,6,1]
        rightTotal = 1
        rightProduct = [1 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            rightTotal *= nums[i+1]
            rightProduct[i] = rightTotal

        # print(rightProduct)

        res = []
        for i in range(len(nums)):
            res.append(leftProduct[i] * rightProduct[i])
        return res
