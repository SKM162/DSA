# we only have non decreasing order (we won't be swapping to preserve the order), the next will definitely be the next higher unique value.
# one pointer tracks the position to be replaced in each iteration.
# one pointer iterates through the array to find next greater.

# let i move through the elements. the current position is always pointing to something to be substituted.
# replace anything different than the current position. if greater than previous move position.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        for i in range(1, len(nums)):
            # ensure p points to the place to be substituted always.
            while p < len(nums) and nums[p] > nums[p-1]:
                p += 1
            # all elements are unique
            if p == len(nums):
                return p
            if nums[i] > nums[p-1]:
                nums[p] = nums[i]
        # # handles moving position for the last value.
        while p < len(nums) and nums[p] > nums[p-1]:
                p += 1
        return p




