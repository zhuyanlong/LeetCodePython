class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        cnt = 0
        for item in hours:
            if item >= target:
                cnt += 1
        return cnt
    
def main():
    hours = [0,1,2,3,4]
    target = 2
    sol = Solution()
    sol.numberOfEmployeesWhoMetTarget(hours, target)

main()