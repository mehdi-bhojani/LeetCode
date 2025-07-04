#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if(val == "."):
                    continue

                if(val in row[r]):
                    return False
                row[r].add(val)

                if(val in col[c]):
                    return False
                col[c].add(val)

                curr_box = int(r/3)*3 + int(c/3)
                if(val in box[curr_box]):
                    return False
                box[curr_box].add(val)
        
        return True


# @lc code=end

