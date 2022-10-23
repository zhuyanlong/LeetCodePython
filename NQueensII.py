#这个题目应该有更简单的做法，但我还没想到
class Solution:
    def totalNQueens(self, n):
        res=[]
        for i in range(n):
            stack=[(0,i)]
            board=[]
            while stack:
                top=stack.pop()
                while len(board)!=top[0]:
                    board.pop()
                board.append(top[1])
                position=list(range(n-1,-1,-1))
                for i in position:
                    if self.check(board,i):
                        stack.append((len(board),i))
                if len(board)==n:
                    res.append(board.copy())
        output=len(res)
        return output

    def check(self,board,j):
        k=len(board)
        for i in range(k):
            if board[i]==j:
                return False
            if j==board[i]+k-i or j==board[i]-(k-i):
                return False
        return True


def main():
    s=Solution()
    output=s.solveNQueens(4)
    print(output)

main()