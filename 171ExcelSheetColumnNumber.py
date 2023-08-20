class Solution:
    def titleToNumber(self, columnTitle):
        num = len(columnTitle)
        reverseColumn = "".join(reversed(columnTitle))
        res = 0
        for i in range(num):
            res += (ord(reverseColumn[i]) - ord('A') + 1) * pow(26, i)
        return res
    
def main():
    columnTitle = "A"
    sol = Solution()
    print(sol.titleToNumber(columnTitle))
    
main()