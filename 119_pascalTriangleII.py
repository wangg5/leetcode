class Solution:
    def getRow(self, rowIndex):
        l = []
        if rowIndex == 0:
            l.append([1])
            return l
        if rowIndex == 1:
            l.append([1])
            l.append([1, 1])
            return l[1]
        l.append([1])
        l.append([1, 1])
        rowI = rowIndex
        while rowI >= 2:
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
            rowI -= 1

        return l[rowIndex]

g = Solution()
rel = g.getRow(4)
print("rel = ", rel)