class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mpoint = m - 1
        npoint = n - 1
        point = m + n - 1
        while npoint >= 0:
            if mpoint < 0:
                nums1[0 : point + 1] = nums2[0 : point + 1]
                break
            elif nums1[mpoint] >= nums2[npoint]:
                nums1[point] = nums1[mpoint]
                mpoint -= 1
            else:
                nums1[point] = nums2[npoint]
                npoint -= 1
            point -= 1