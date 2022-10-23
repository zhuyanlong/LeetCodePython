class Solution:
    def spiralOrder(self, matrix):
        res=[]
        leftToRight=1
        upToDown=0
        rightToLeft=0
        downToUp=0
        left=0
        right=len(matrix[0])-1
        up=0
        down=len(matrix)-1
        count=(right+1)*(down+1)
        while count!=len(res):
            print(res)
            if leftToRight==1:
                for j in range(left,right+1):
                    res.append(matrix[up][j])
                leftToRight=0
                upToDown=1
                up+=1
            if upToDown==1:
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                upToDown=0
                rightToLeft=1
                right-=1
            if rightToLeft==1:
                for j in range(right,left-1,-1):
                    res.append(matrix[down][j])
                rightToLeft=0
                downToUp=1
                down-=1
            if downToUp==1:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
                downToUp=0
                leftToRight=1
        print(res)
        return res

def main():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    sol=Solution()
    sol.spiralOrder(matrix)

main()