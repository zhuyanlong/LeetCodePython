class Solution:
    def compareVersion(self, version1, version2):
        v1=version1.split(".")
        v2=version2.split(".")
        for i in range(len(v1)):
            v1[i]=int(v1[i])
        for j in range(len(v2)):
            v2[j]=int(v2[j])
        i=0
        while i!=len(v1) and i!=len(v2):
            if v1[i]<v2[i]:
                return -1
            elif v1[i]>v2[i]:
                return 1
            else:
                i+=1

        if i<len(v1):
            for j in range(i,len(v1)):
                if v1[j]!=0:
                    return 1
            return 0
        elif i<len(v2):
            for j in range(i,len(v2)):
                if v2[j]!=0:
                    return -1
            return 0
        else:
            return 0    

def main():
    version1="1.01"
    version2="1.001"
    sol=Solution()
    print(sol.compareVersion(version1,version2))

main()