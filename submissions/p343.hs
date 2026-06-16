module Solution (integerBreak) where

integerBreak :: Int -> Int
integerBreak 2 = 1
integerBreak 3 = 2
integerBreak n
  | n `mod` 3 == 0 = 3 ^ (n `div` 3)
  | n `mod` 3 == 1 = 4 * 3 ^ ((n - 4) `div` 3)
  | otherwise      = 2 * 3 ^ ((n - 2) `div` 3)
