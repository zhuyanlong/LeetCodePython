class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1=len(nums1)
        len2=len(nums2)
        i=0
        j=0
        length=len1+len2
        # 用来标记总位数是奇数位还是偶数位
        flag=0
        if length%2==0:
            flag=1
        m=length//2 
        k=0
        while i!=len1 and j!=len2:
            
            
