class Solution:
    def maximumNumberOfStringPairs(self, words):
        wordsSet = set()
        res = 0
        for item in words:
            reversedItem = ''.join(reversed(item))
            if reversedItem in words and (item not in wordsSet) and (reversedItem not in wordsSet) and item != reversedItem:
               res += 1
               wordsSet.add(item) 
        return res
    
def main():
    words = ["aa","ab"]
    sol = Solution()
    res = sol.maximumNumberOfStringPairs(words)
    print(res)

main()