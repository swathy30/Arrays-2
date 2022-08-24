class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m= len(board)
        n= len(board[0])
        
        dirs = [[1,0],[-1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        
        for i in range(m):
            for j in range(n):
                count=0
                for r,c in dirs:
                    nr= i+r
                    nc= j+c
                    if nr>=0 and nc>=0 and nr<m and nc<n:
                        if board[nr][nc]==1 or board[nr][nc]==-1:
                            count +=1
                if board[i][j]==1:
                    if count>3 or count<2:
                        board[i][j] = -1
                else:
                    if count==3:
                        board[i][j]=2
                        
        for i in range(m):
            for j in range(n):
                if board[i][j]>0:
                    board[i][j]=1
                else:
                    board[i][j]=0