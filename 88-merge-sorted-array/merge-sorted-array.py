class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        A = m - 1
        B = n - 1
        C = m + n - 1

        while B >= 0:
            if A >= 0 and nums1[A] > nums2[B]:
                nums1[C] = nums1[A]
                A -= 1
            else:
                nums1[C] = nums2[B]
                B -= 1
            C -= 1