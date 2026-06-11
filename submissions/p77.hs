module Solution (combine) where

combine :: Int -> Int -> [[Int]]
combine n k = go 1 k
  where
    go start 0 = [[]]
    go start r
      | start > n = []
      | otherwise =
          [start : rest | rest <- go (start + 1) (r - 1)] ++
          go (start + 1) r
