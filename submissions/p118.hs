module Solution (generate) where

generate :: Int -> [[Int]]
generate n = take n rows
  where
    rows = [1] : map nextRow rows
    nextRow r = zipWith (+) (0 : r) (r ++ [0])
