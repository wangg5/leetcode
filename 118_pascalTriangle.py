class Solution:
    def generate(self, numRows):
        l = []
        if numRows == 1:
            l.append([1])
            return l
        if numRows == 2:
            l.append([1])
            l.append([1, 1])
            return l
        l.append([1])
        l.append([1, 1])
        while numRows > 2:
            temp = []
            last_row = l[len(l) -1]
            new_row = []
            new_row.append(1)
            print("len l = ", len(l))
            for i in range(1, len(l), 1):
                v = last_row[i-1] + last_row[i]
                #print(v)
                new_row.append(v)
            new_row.append(1)
            l.append(new_row)
            numRows -= 1
        return l
g = Solution()
rel = g.generate(5)
print("rel = ", rel)