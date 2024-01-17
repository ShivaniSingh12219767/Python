class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        p=len(nums1)
        nums1.extend(nums2)
        l=len(nums1)
        nums1.sort()
        print(nums1)
        if l%2!=0:
            return nums1[l//2]
        else:
            s=(nums1[l//2]+nums1[(l//2)+1])/2
            return s
obj1=Solution()
print(obj1.findMedianSortedArrays([1,2],[3,4]))