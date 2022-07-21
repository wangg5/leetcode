class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def twoSum(self):
        out = []
        for i in range(len(self.nums)):
            print("i= ", nums[i])
            #if self.nums[i] <= self.target:
            for j in range(i+1, len(self.nums)):
                print("i+1 = ", i+1)
                if self.nums[i] + self.nums[j] == self.target:
                    print("j = ", nums[j])
                    out.append(i)
                    out.append(j)
                    break
            if len(out) > 0:
                return out
                #break

nums = [2,7,11,15]
target = 9
c1 = Solution(nums, target)
out = c1.twoSum()
print(out)