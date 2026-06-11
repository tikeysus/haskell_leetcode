module Solution (combinationSum3) where

combinationSum3 :: Int -> Int -> [[Int]]
combinationSum3 k n = go 1 k n
  where
    go _ 0 0 = [[]]
    go _ 0 _ = []
    go start r remaining
      | start > 9 || start > remaining = []
      | otherwise =
          [start : rest | rest <- go (start + 1) (r - 1) (remaining - start)] ++
          go (start + 1) r remaining
