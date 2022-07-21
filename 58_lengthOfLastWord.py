class Solution:
    def lengthOfLastWord(self, s):
        ss= s.split()
        length = len(ss)
        print("ss = ", ss)
        lastWord = ss[length-1]
        return len(lastWord)

s =  "luffy is still joyboy"
llw = Solution()
rel = llw.lengthOfLastWord(s)
print("rel = ", rel)