class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #idea:
        #list of sets? fist 9 ros, next 9 columns, next 9 squares
        # add each number to its 3 list spots. if it appears in that set or is not in 1-9 the return false
        #possible drawbacks? big boy list
        #benefits. only need to go though once

        lis= list(set() for i in range (27))
        r_buff = 0
        c_buff= 9
        box_buff= 18
        for r in range(0,9):
            for c in range(0,9):
                val = board[r][c]
                #check row
                if val != '.':
                    if val in lis[r_buff+r]:
                        return False
                    else:
                        lis[r_buff+r].add(val) ## i checked add and in for sets
                #check col
                if val != '.':
                    if val in lis[c_buff+c]:
                        return False
                    else:
                        lis[c_buff+c].add(val)
                #check box
                box = (c//3) + 3* (r// 3)
                if val != '.':
                    if val in lis[box_buff+box]:
                        return False
                    else:
                        lis[box_buff+box].add(val)
        return True
                    
