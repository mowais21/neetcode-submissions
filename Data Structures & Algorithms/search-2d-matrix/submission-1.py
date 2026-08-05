class Solution:
    # matrix: 2D integer array
    # returns: true if target exists within the matrix, false otherwise
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # properties: each row is sorted in a non-decreasing order
        # first integer of a row is greater than the last integer of the previous row

        # algorithm:
        # 1. find a matching row using binary search (element can only be in 1 row due to the ordering properties)
        # 2. perform a binary search within the row

        # searches for the correct row to perform binary lookup in
        def binarySearchForRow(matrix, target):
            u = 0
            d = len(matrix) - 1

            while u <= d:
                mid = u + ((d - u) // 2)

                # in the upper half
                if target < matrix[mid][0]:
                    d = mid - 1
                elif target > matrix[mid][-1]:
                    u = mid + 1
                else:
                    return mid

            return -1

        def binarySearchInRow(row, target):
            l = 0
            r = len(row) - 1

            while l <= r:
                mid = l + ((r-l) // 2)
                curr = row[mid]

                if target > curr:
                    l = mid + 1
                elif target < curr:
                    r = mid - 1
                else:
                    return mid

            return -1

        row = binarySearchForRow(matrix, target)

        if row >= 0:
            col = binarySearchInRow(matrix[row], target)

            if col >= 0:
                return True

        return False


