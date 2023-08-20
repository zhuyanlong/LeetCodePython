class Solution:
    def splitWordsBySeparator(self, words, separator):
        wordsDic = {}
        for i in range(len(words)):
            wordsDic[i] = words[i].split(separator)
        res = []
        for key in wordsDic:
            for item in wordsDic[key]:
                if item != "":
                    res.append(item)
        print(res)
        
def main():
    words = ["|||"]
    separator = "|"
    sol = Solution()
    sol.splitWordsBySeparator(words, separator)

main()