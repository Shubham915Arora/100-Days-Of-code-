class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j] :
                    if nums1[i] not in  l:
                        l.append(nums1[i])
        return l