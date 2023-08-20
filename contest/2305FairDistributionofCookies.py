# 抄了答案 没看懂怎么写的
class Solution:
    def distributeCookies(self, cookies, k):
        if len(cookies) == k:
            return max(cookies)

        def bt(i, path):
            if i == len(cookies):
                return max(path)
            res = float('inf')
            for j in range(k):
                path[j] += cookies[i]
                res = min(res, bt(i+1, path))
                path[j] -= cookies[i]
            return res

        path = [0] * k
        return bt(0, path)
    
def main():
    cookies = [8, 15, 10, 20, 8]
    k = 2
    sol = Solution()
    res = sol.distributeCookies(cookies, 2)
    print(res)

main()