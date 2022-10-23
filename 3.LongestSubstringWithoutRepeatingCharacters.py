#寻找最长不重复字符串，采用双指针复杂度O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        mac=0
        i=0
        tmp=[]
        while i!=len(s):
            if s[i] in tmp:
                tmp=tmp[tmp.index(s[i])+1:]
            tmp.append(s[i])
            if len(tmp)>mac:
                mac=len(tmp)
            i+=1
        return mac


def main():
    s=Solution()
    t="aab"
    print(s.lengthOfLongestSubstring(t))

main()