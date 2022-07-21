
"""
https://appdividend.com/2021/06/14/how-to-convert-python-int-to-binary-string/

"""
class Solution:
    def hammingWeight(self, n):
        bits = 0
        while n:
            bits += n & 1
            n >>= 1
        return bits

hw = Solution()
rel = hw.hammingWeight(9)
print("rel = ", rel)

"""
        getbinary = lambda x, n: format(x, 'b').zfill(n)
        s = getbinary(11, 32)
        n_1_bit = 0
        for i in range(len(s)):
            if s[i] == "1":
                n_1_bit += 1
        return n_1_bit
"""