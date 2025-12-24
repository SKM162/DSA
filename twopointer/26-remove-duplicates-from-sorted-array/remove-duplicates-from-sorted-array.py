# given a non decreasing array, the next greatest element always occurs 
# when the previous element is lesser. we just need to find the deviations where the element steps up.
# we can assume only one unique element exists at first at 0
# only increase the position on finding the next high.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0 
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                #higher element found
                p += 1
                nums[p] = nums[i]
        return p + 1
        