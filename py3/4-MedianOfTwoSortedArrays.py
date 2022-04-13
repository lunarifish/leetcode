# 2021-12-29 17:38
# Runtime 172ms(6.2%)
# Memory N/A

##
# 好像是因为还不知道sorted()和list.sort()所以才造了个排序
# 然后这个qsort是哪儿抄的???????:)))))
# 还有就是我给递归写一个return 0的样子真的很帅
###

class Solution:
    def Qsort(array, start, end):
        if start >= end:
            return 0
        mid_data, left, right = array[start], start, end
        while left < right:
            while array[right] >= mid_data and left < right:
                right -= 1
            array[left] = array[right]
            while array[left] < mid_data and left < right:
                left += 1
            array[right] = array[left]
        array[left] = mid_data
        Solution.Qsort(array, start, left-1)
        Solution.Qsort(array, left+1, end)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        length = len(merged)
        Solution.Qsort(merged, 0, length - 1)
        if length % 2 == 1:
            median = merged[int(length / 2)]
        else:
            median = (merged[int(length / 2 - 1)] + merged[int(length / 2)]) / 2
        return float(median)
