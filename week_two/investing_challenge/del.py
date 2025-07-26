from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def helper(k, i, j, not_allowed=None):
            if k > len(word) - 1:
                return False

            if board[i][j] != word[k]:
                return False

            if k == len(word)-1:
                return True

            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]

                if (ni, nj) == not_allowed:
                    continue

                if ni > -1 and ni < len(board) and nj > -1 and nj < len(board[0]):
                    if helper(k+1, ni, nj, (i, j)):
                        return True

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(0, i, j):
                    return True

        return False


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
      ["A", "D", "E", "E"]], "ABCB"))
