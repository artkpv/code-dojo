#!python3


class Solution:

    def permutation(nums):
        if not nums:
            yield []  # to start combining
        for i in range(len(nums)):
            for p in Solution.permutation(nums[:i] + nums[i+1:]):
                yield [nums[i]] + p

    def permute(self, nums):
        return list(Solution.permutation(nums))


if __name__ == '__main__':
    s = Solution()
    res = s.permute([1,2,3])
    print('Result', res)
    assert res == [
        [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
    ]
