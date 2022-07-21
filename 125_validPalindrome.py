class Solution:
    def validPalindrome(self, s):
        alphabet = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6","7","8","9"]
        ns = ""
        for i in range(len(s)):
            if s[i].lower() in alphabet:
                ns += s[i].lower()
        print("ns = ", ns)
        while len(ns) >= 1:
            if ns[0] == ns[len(ns) -1]:
                ns = ns[1:len(ns)-1]
            else:
                return False
        return True

s = "A man, a plan, a canal: Panama"
vp = Solution()
rel = vp.validPalindrome(s)
print("rel = ", rel)


"""
    def rec_validPalindrome(self, ns):
        print("ns = ", ns)
        if len(ns) == 0:
            return True
        elif len(ns) == 1:
            return True
        else:
            if ns[0] == ns[len(ns)-1]:
                return self.rec_validPalindrome(ns[1:len(ns)-1])
            else:
                return False
"""