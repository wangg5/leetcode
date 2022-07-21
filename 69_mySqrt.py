class Solution:
    def mySqrt(self, x):
        left, right = 0, x + 1
        mid = (left + right)//2
        while left < right:
            mid = (left + right)//2
            s = mid**2
            if s == x:
                return mid
            elif (right - left == 1) and left ** 2 < x and right ** 2 > x:
                return left
            elif s < x: # go to right
                left = mid
            elif s > x: # go to left
                right = mid


mq = Solution()
rel = mq.mySqrt(1000)
print("rel = ", rel)

"""
#================== recursion version ========need more space=======
    def mySqrt(self, x):
        left, right = 0, x+1
        mid = (left + right)//2
        return self.rec_mySqrt(left, mid, right, x)

    def rec_mySqrt(self, left, mid, right, x):
        s = mid ** 2
        if s == x:
            return mid
        elif (right - left == 1) and left**2 < x and right**2 > x:
            return left
        elif s < x:
            left = mid
            #right = x + 1
            mid = (left + right)//2
            return self.rec_mySqrt(left, mid, right, x)
        elif s > x:
            right = mid
            mid = (left + right)//2
            return self.rec_mySqrt(left, mid, right, x)
"""