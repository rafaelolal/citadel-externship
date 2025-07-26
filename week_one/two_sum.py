class Solution:
    def twoSum(self, nums, target):
        c = 0
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                c += 1
                if nums[j] + nums[j - i] == target:
                    return [j, j - i]

        print(c)
        return None


s = Solution()
print(s.twoSum([2, 11, 15, 30, 7, 50, 60], 50))
