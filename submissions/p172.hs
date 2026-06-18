module Solution (trailingZeroes) where

trailingZeroes :: Int -> Int
trailingZeroes 0 = 0
trailingZeroes n = n `div` 5 + trailingZeroes (n `div` 5)
