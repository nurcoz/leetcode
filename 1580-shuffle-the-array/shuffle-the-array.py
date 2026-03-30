class Solution(object):
    def shuffle(self, nums, n):
        ans = []
        x = len(nums) -1
        i = 0
        while len(ans)<len(nums):
            if i <= x:
                ans.append(nums[i])
            else:
                ans.append(nums[(i % x)])
                i -= x
            i += n
        return ans

        