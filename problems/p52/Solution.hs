module Solution (totalNQueens) where

import qualified Data.Set as Set

totalNQueens :: Int -> Int
totalNQueens n = length (place n 0 Set.empty Set.empty Set.empty)

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
