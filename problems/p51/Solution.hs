module Solution (solveNQueens) where

solveNQueens :: Int -> [[String]]
solveNQueens n = map (toBoard n) (place n 0 [] [] [])

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

toBoard :: Int -> [Int] -> [String]
toBoard n = map (\c -> replicate c '.' ++ "Q" ++ replicate (n - c - 1) '.')
