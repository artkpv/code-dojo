#!python3
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        P = [nums[:]]
        while True:
            suf = n - 1
            while suf - 1 >= 0 and nums[suf-1] >= nums[suf]:
                suf -= 1
            if suf == 0:
                break
            _, i = min((el,i) for i, el in enumerate(nums[suf:]) if el > nums[suf-1])
            i += suf
            nums[suf-1], nums[i] = nums[i], nums[suf-1]
            nums = nums[:suf] + sorted(nums[suf:])
            P += [nums[:]]
        return P
