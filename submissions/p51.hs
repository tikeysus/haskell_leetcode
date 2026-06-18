module Solution (solveNQueens) where

import qualified Data.Set as Set

solveNQueens :: Int -> [[String]]
solveNQueens n = map (toBoard n) (place n 0 Set.empty Set.empty Set.empty)

place :: Int -> Int -> Set.Set Int -> Set.Set Int -> Set.Set Int -> [[Int]]
place n row cols diag1 diag2
  | row == n  = [[]]
  | otherwise =
      [ col : rest
      | col  <- [0..n-1]
      , not (Set.member col cols)
      , not (Set.member (row - col) diag1)
      , not (Set.member (row + col) diag2)
      , rest <- place n (row+1)
                  (Set.insert col cols)
                  (Set.insert (row-col) diag1)
                  (Set.insert (row+col) diag2)
      ]

toBoard :: Int -> [Int] -> [String]
toBoard n = map (\c -> replicate c '.' ++ "Q" ++ replicate (n - c - 1) '.')
