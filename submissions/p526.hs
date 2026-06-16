module Solution (countArrangement) where

import Data.Bits

countArrangement :: Int -> Int
countArrangement n = go 1 (0 :: Int)
  where
    go pos used
      | pos > n   = 1
      | otherwise = sum [ go (pos+1) (used .|. bit k)
                        | k <- [1..n]
                        , not (testBit used k)
                        , k `mod` pos == 0 || pos `mod` k == 0 ]
