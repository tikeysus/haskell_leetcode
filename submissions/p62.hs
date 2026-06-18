module Solution (uniquePaths) where

uniquePaths :: Int -> Int -> Integer
uniquePaths m n = product [s - k + 1 .. s] `div` product [1 .. k]
  where
    s = toInteger (m + n - 2)
    k = toInteger (min (m - 1) (n - 1))
