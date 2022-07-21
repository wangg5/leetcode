class Solution:
    def addBinary(self, a, b):
        a = list(a)
        b = list(b)
        len_a = len(a) - 1
        len_b = len(b) - 1
        add = "0"
        rel = ""
        while len_a >= 0:
            if add == "0":
                if a[len_a] == "1" and b[len_b] == "1":
                    a[len_a] = "0"
                    add = "1"
                elif a[len_a] == "0" and b[len_b] == "1":
                    a[len_a] = "1"
                    add = "0"
                elif a[len_a] == "1" and b[len_b] == "0":
                    a[len_a] = "1"
                    add = "0"
                elif a[len_a] == "0" and b[len_b] == "0":
                    a[len_a] = "0"
                    add = "0"
            else:
                if a[len_a] == "1" and b[len_b] == "0":
                    a[len_a] = "0"
                    add = "1"
                elif a[len_a] == "0" and b[len_b] == "1":
                    a[len_a] = "0"
                    add = "1"
                elif a[len_a] == "0" and b[len_b] == "0":
                    a[len_a] = "1"
                    add = "0"
                elif a[len_a] == "1" and b[len_b] == "1":
                    a[len_a] = "1"
                    add = "1"
            len_a -= 1
            len_b -= 1
            if len_a < 0 and len_b >= 0:
                if add == "1":
                    truncate_index = len_b + 1
                    while len_b >= 0:
                        if add == "1":
                            if b[len_b] == "1":
                                b[len_b] = "0"
                                add == "1"
                            else:
                                b[len_b] = "1"
                                add = "0"
                            len_b -= 1
                        else:
                            break

                    if len_b < 0 and add == "1":
                        rel = ["1"] + b[0:truncate_index] + a
                    else:
                        rel = b[0:truncate_index] + a
                else:
                    rel = b[0:len_b+1] + a
                break
            elif len_a >=0 and len_b < 0:
                if add == "1":
                    # check the rest of a
                    truncate_index = len_a + 1
                    while len_a >= 0:
                        if add == "1":
                            if a[len_a] == "1":
                                a[len_a] = "0"
                                add = "1"
                            else:
                                a[len_a] = "1"
                                add = "0"
                            len_a -= 1
                        else:
                            break
                    if len_a < 0 and add == "1":
                        rel = ["1"] + a
                    else:
                        rel = a
                else:
                    rel = a
                break
            elif len_a == -1 and len_b == -1:
                if add == "1":
                    rel = ["1"] + a
                else:
                    rel = a
        rel = "".join(rel)
        return rel
s1 = "011"
s2 = "1111"
ab = Solution()
rel = ab.addBinary(s1, s2)
print("rel = ", rel)