#官方提示贪心法，我觉得可以用暴力求解，目前想不到更好的解决方案了
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost)>sum(gas):
            return -1
        for i in range(len(gas)):
            if gas[i]>=cost[i]:
                j=i
                while j!=i:
                    k=(j+1)%len(gas)
                    if gas[j]-cost[j]+gas[k]<cost[k]:
                        continue
                    else:
                        j=(j+1)%len(gas)

        return -1

def main():
    # gas  = [1,2,3,4,5]
    # cost = [3,4,5,1,2]
    # gas  = [2,3,4]
    # cost = [3,4,3]
    gas  = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    s=Solution()
    print(s.canCompleteCircuit(gas,cost))

main()