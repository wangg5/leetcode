class Solution:
    def romanToInt(self, s):
        rel = 0
        return self.rec_romanToInt(s, rel)
    def number(self, s):
        if s == "I":
            return 1
        elif s == "V":
            return 5
        elif s == "X":
            return 10
        elif s == "L":
            return 50
        elif s == "C":
            return 100
        elif s == "D":
            return 500
        elif s == "M":
            return 1000
    def rec_romanToInt(self, s, rel):
        if len(s) == 1:
            rel += self.number(s)
            return rel
        elif len(s) == 0:
            return rel
        else: # lenght of s is greater than 1
            # process one number
            if s[0] == "I" and s[1] == "V":
                rel += 4
                return self.rec_romanToInt(s[2:], rel)
            elif s[0] == "I" and s[1] == "X":
                rel += 9
                return self.rec_romanToInt(s[2:], rel)
            elif s[0] == "X" and s[1] == "L":
                rel += 40
                return self.rec_romanToInt(s[2:], rel)
            elif s[0] == "X" and s[1] == "C":
                rel += 90
                return self.rec_romanToInt(s[2:], rel)
            elif s[0] == "C" and s[1] == "D":
                rel += 400
                return self.rec_romanToInt(s[2:], rel)
            elif s[0] == "C" and s[1] == "M":
                rel += 900
                return self.rec_romanToInt(s[2:], rel)
            elif s[0] == "I":
                rel += 1
                return self.rec_romanToInt(s[1:], rel)
            elif s[0] == "V":
                rel += 5
                return self.rec_romanToInt(s[1:], rel)
            elif s[0] == "X":
                rel += 10
                return self.rec_romanToInt(s[1:], rel)
            elif s[0] == "L":
                rel += 50
                return self.rec_romanToInt(s[1:], rel)
            elif s[0] == "C":
                rel += 100
                return self.rec_romanToInt(s[1:], rel)
            elif s[0] == "D":
                rel += 500
                return self.rec_romanToInt(s[1:], rel)
            elif s[0] == "M":
                rel += 1000
                return self.rec_romanToInt(s[1:], rel)

s = "IX"
rt = Solution()
rel = rt.romanToInt(s)
print("rel = ", rel)