# class Solution:
#     def permute(self, nums):
#         result=[nums[0]]
#         for i in range(1,len(nums)):
#             result=self.getArrayInsertArray(result,nums[i])
#         return result

#     def getArrayInsertS():

#     def getArrayInsertArray(self,array,item):
#         index=0
#         re_array=[]
#         while index<len(array):
#             index+=1

#         return re_array

# def main():
#     nums = [1,2,3]
#     sol=Solution()
#     sol.permute(nums)

# main

def getArrayInsertCharToStr(STR,CHAR):
    arr =[]
    s_len = len(STR)
    index =0
    while index <= s_len:
        #分割字符串
        arr.append(STR[:index]+CHAR+STR[index:s_len])
        index = index + 1
    return arr

def getArrayInsertCharToArray(array,CHAR):
    index = 0
    re_array = []
    while index < len(array):
        re_array = re_array + getArrayInsertCharToStr(array[index],CHAR)
        index = index + 1
    return re_array

def getPermutation(STR):
    resultArr = [STR[0]]
    for item in STR[1:]:
        resultArr = getArrayInsertCharToArray(resultArr,item)
    return resultArr

print(getPermutation('abc'))

