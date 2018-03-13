class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = int((m + n - 1) / 2)
        lo, hi = 0, m
        while lo < hi:
            i = int((lo + hi) / 2)
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
                

if __name__ == '__main__':
    so = Solution()
    nums1 = [1, 12, 15, 26, 38]
    nums2 = [2, 13, 17, 30, 45, 50]
    print(so.findMedianSortedArrays(nums1,nums2))
