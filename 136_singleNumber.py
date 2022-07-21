# 1. sort this list, than loop through the sorted list. nums[i] == nums[i+1]??
# 2. hashmap

class Solution:
    def singleNumber(self, nums):
        rel = 0
        for i in nums:
            rel = i^rel
        return rel