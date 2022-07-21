class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        n = 0
        while j < len(nums):
            if nums[i] >= nums[j]:
                j += 1
            else:
                # swap nums[i+1] and nums[j]
                temp = nums[j]
                nums[j] = nums[i+1]
                nums[i+1] = temp
                n += 1
                i += 1
                j += 1
        k = n +1
        print("nums = ", nums)
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
rmv = Solution()
rel = rmv.removeDuplicates(nums)
print("rel = ", rel)