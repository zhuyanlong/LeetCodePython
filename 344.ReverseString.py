class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        print(s)
def main():
    s=["H","a","n","n","a","h"]
    sol=Solution()
    sol.reverseString(s)

main()