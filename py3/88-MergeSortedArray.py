# 2022-05-13 17:12:57
# Runtime 40ms(46.4%)
# Memory 14.9mb(88.2%)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index, i in enumerate(sorted(nums1[:m] + nums2)):
            nums1[index] = i
