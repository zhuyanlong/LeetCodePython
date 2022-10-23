class Solution:
    def findDifference(self, nums1, nums2):
        a=[]
        b=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                if nums1[i] not in a:
                    a.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                if nums2[i] not in b:
                    b.append(nums2[i])
        answer=[]
        answer.append(a)
        answer.append(b)
        return answer

def main():
    sol=Solution()
    nums1=[1,2,3,3]
    nums2=[1,1,2,2]
    ans=sol.findDifference(nums1,nums2)
    print(ans)

main()