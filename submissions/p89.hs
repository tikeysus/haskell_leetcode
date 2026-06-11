module Solution (grayCode) where

import Data.Bits (xor, shiftR)

grayCode :: Int -> [Int]
grayCode n = [i `xor` (i `shiftR` 1) | i <- [0..2^n - 1]]
