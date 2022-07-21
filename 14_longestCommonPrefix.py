class Solution:
    def longestCommonPrefix(self, strs):
        is_common_pre = True
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""
        else:
            first_word = strs[0]
            print("first_word = ", first_word)
            index = 0
            for i in range(len(first_word)):
                is_common_pre = True
                print("first_word[i] = ", first_word[i])
                for j in range(1, len(strs)):
                    if i >= len(strs[j]):
                        is_common_pre = False
                        break
                    if first_word[i] != strs[j][i]:
                        is_common_pre = False
                        break
                index = i
                if not is_common_pre:
                    break
            #index = i
            if is_common_pre:
                index += 1

            print("i = ", i)
            return first_word[0:index]
s = ["flower","flow","flight"]
#s = ["flower","flower","flower","flower"]
s = ["ab", "a"]
lcp = Solution()
rel = lcp.longestCommonPrefix(s)
print("rel = ", rel)
