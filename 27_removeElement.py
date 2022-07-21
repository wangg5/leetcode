class Solution:
    def removeElement(self, nums, val):
        j = i = len(nums) -1
        n = 0
        has_swap = False
        while j >= 0:
            if nums[j] == val:
                 # swap
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i -= 1
                j -= 1
                n += 1
                has_swap = True
            if has_swap == True:
                has_swap = False
            else:
                j -= 1

        k = len(nums) - n # how many elements are not equal val
        return k


nums = [3, 2, 2, 3]
val = 3
rmv = Solution()
rel = rmv.removeElement(nums, val)
print("rel = ", rel)
