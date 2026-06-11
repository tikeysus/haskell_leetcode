module Solution (totalNQueens) where

totalNQueens :: Int -> Int
totalNQueens n = length (place n 0 [] [] [])

place :: Int -> Int -> [Int] -> [Int] -> [Int] -> [[Int]]
place n row cols diag1 diag2
  | row == n  = [[]]
  | otherwise =
      [ col : rest
      | col  <- [0..n-1]
      , col  `notElem` cols
      , (row - col) `notElem` diag1
      , (row + col) `notElem` diag2
      , rest <- place n (row+1) (col:cols) ((row-col):diag1) ((row+col):diag2)
      ]
