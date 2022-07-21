class Solution:
    def plusOne(self, digits):
        length = len(digits)
        print("length = ", length)
        for i in range(length-1, -1, -1):
            print("digits[i] = ", digits[i])
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                print("i = ", i)
                if i == 0:
                    digits.insert(0, 1)
        return digits

digits = [1,2,3]
po = Solution()
rel = po.plusOne(digits)
print("rel = ", rel)