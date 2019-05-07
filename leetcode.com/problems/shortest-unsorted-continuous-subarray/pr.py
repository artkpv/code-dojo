class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        if not nums or len(nums) == 1:
            return 0
        inx = 1
        lo = None
        hi = None
        while inx < len(nums):
            # search next unsorted
            if nums[inx-1] > nums[inx]:
                # find left ID to put nums[inx]
                left = inx-1 if lo is None else lo
                while 0 < left and nums[left-1] > nums[inx]:
                    left -= 1
                lo = left

                # find right ID for num[inx-1]
                right = inx if hi is None else max(inx, hi)
                while right < len(nums)-1 and nums[inx-1] > nums[right+1]:
                    right += 1
                hi = right
            inx += 1
            print(lo, hi)
        return 0 if lo is None else hi - lo + 1

"""
None None
1 2
1 2
1 2
1 3
1 3


1 3 5 4 2
      ^
inx lo hi
1
2
3   2  3
"""
