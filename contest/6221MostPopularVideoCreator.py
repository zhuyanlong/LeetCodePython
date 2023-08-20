# 超时了
class Solution:
    def mostPopularCreator(self, creators, ids, views):
        idsViewDict = {}
        idsDict = {}
        viewsDict = {}
        for i in range(len(creators)):
            if creators[i] in viewsDict:
                viewsDict[creators[i]] += views[i]
            else:
                viewsDict[creators[i]] = views[i]
        maxKey = []
        maxValue = 0
        for key in viewsDict.keys():
            if viewsDict[key] > maxValue:
                maxValue = viewsDict[key]
                maxKey = []
                maxKey.append(key)
            elif viewsDict[key] == maxValue:
                maxKey.append(key)
        for i in range(len(creators)):
            if creators[i] in maxKey:
                if creators[i] not in idsDict:
                    idsDict[creators[i]] = []
                idsDict[creators[i]].append(ids[i])
        for i in range(len(ids)):
            idsViewDict[ids[i]] = views[i]
        res = []
        for key in maxKey:
            maxValue = 0
            resItem = idsDict[key][0]
            for item in idsDict[key]:
                
                if idsViewDict[item] > maxValue:
                    maxValue = idsViewDict[item]
                    resItem = item
            res.append([key, resItem])
        print(res)
        return res
        
def main():
    sol = Solution()
    creators = ["a"]
    ids = ["a"]
    views = [0]
    sol.mostPopularCreator(creators, ids, views)
    
main()        