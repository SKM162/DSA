#26. Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=two-pointers
# NOTE:
# Non decreasing - duplicates in sorted array.
# increasing - strictly ascending - no duplicates.

# Given a non decreasing array, the next greatest element always occurs -
# when the previous element is lesser. we just need to find the deviations where the element steps up.
# we have to collect all unique items at start of the array.
# THE MORE IMPORTANT TASK IS TO FIRST FIND THE NEXT UNIQUE ELEMENT.
# we can assume only one unique element exists at first at 0
# then only increase the position on finding the next higher element.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    # The first element will be the unique by default.
        p = 0 
        # right pointer tracks the next element.
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                # higher element found
                # shift left pointer
                p += 1
                nums[p] = nums[i]
        return p + 1
        
