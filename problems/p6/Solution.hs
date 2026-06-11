module Solution (convert) where

convert :: String -> Int -> String
convert s 1 = s
convert s numRows = concatMap rowChars [0 .. numRows - 1]
  where
    zigzag    = [0 .. numRows - 1] ++ [numRows - 2, numRows - 3 .. 1]
    rowChars r = [c | (row, c) <- zip (cycle zigzag) s, row == r]
