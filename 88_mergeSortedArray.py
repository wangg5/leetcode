class Solution:
    def mergeSortedArray(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = 0
        while (i >= 0 and j >= 0):
            print("i = j =", i, j)
            if nums1[i] >= nums2[j]:
                nums1[m+n-1-k] = nums1[i]
                k += 1
                i -= 1
                print("i = ", i)
            else:
                nums1[m+n-1-k] = nums2[j]
                k += 1
                j -= 1
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1

nums1 = [0]
nums2 = [1]
msa = Solution()
msa.mergeSortedArray(nums1, 0, nums2, 1)
print("nums1 = ", nums1)