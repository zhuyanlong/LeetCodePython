#好愚蠢，不想做了
# class Solution:
#     def addStrings(self, num1, num2):
#         res=''
#         if len(num1)>len(num2):
#             maxnum=num1
#             minnum=num2
#         else:
#             maxnum=num2
#             minnum=num1
#         i=len(minnum)-1
#         while i>=0:
#             carry=0
#             tmp=int(minnum[i])+int(maxnum[i])
#             if tmp>9:
#                 carry=1
#                 tmp=tmp%10
#             res=str(tmp)+res
#             if carry==1:
#                 tmplst=list(maxnum)
#                 tmplst[i]=str(int(tmplst[i])+1)
#                 maxnum="".join(tmplst)
#             i+=1
#         print(maxnum)
#         while i<len(maxnum):
#             print(i)
#             print(maxnum[i])
#             res=maxnum[i]+res
#             i+=1
#         print(res)

def main():
    num1="999"
    num2="99"
    s=Solution()
    s.addStrings(num1,num2)

main()