num = -121
s_num = str(num)
print("num = ", num)
print("s_num = ", s_num[0])

class Solution:
    #def __init__(self):
    def str_isPalindrome(self, str_x):
        if len(str_x) == 0 or len(str_x) == 1:
            return True
        elif str_x[0] != str_x[len(str_x)-1]:
            return False
        else:
            if len(str_x[1:len(str_x)-1]) == 0:
                return True
            else:
                #int_x = int(str_x[1:len(str_x)-1])
                #print(int_x)
                return self.str_isPalindrome(str_x[1:len(str_x)-1])

    def isPalindrome(self, x):
        str_x = str(x)
        print("str_x =", str_x)
        return self.str_isPalindrome(str_x)

i = 1000021
#c = int(i)
#print("c = ", c)
rel = Solution()
ret = rel.isPalindrome(i)
print(ret)