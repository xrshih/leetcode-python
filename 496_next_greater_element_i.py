class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        greater_map = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                greater_map[smaller] = num
            stack.append(num)
        return [greater_map.get(x,-1) for x in nums1]