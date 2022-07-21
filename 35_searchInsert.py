class Solution:
    def searchInsert(self, nums, target):
        index = 0
        return self.insertIndex(nums, target, index)

    def insertIndex(self, nums, target, index):
        if len(nums) == 0:
            return index
        elif len(nums) == 1:
            if nums[0] < target:
                return index + 1
            else:
                return index
        else:
            print("len = ", len(nums))
            i = len(nums)//2
            print("i = ", i)
            if nums[i] <= target:  # go to right half array
                index += i
                return self.insertIndex(nums[i:len(nums)], target, index)
            else:
                #index = i-1
                return self.insertIndex(nums[0:i], target, index)
nums = [1,6,7,8]
target = 9
irt = Solution()
rel = irt.searchInsert(nums, target)
print("rel = ", rel)