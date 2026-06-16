module Solution (getMoneyAmount) where

import Data.Array

getMoneyAmount :: Int -> Int
getMoneyAmount n = dp ! (1, n)
  where
    dp = listArray ((0, 0), (n+1, n+1))
           [if i >= j then 0 else cost i j | i <- [0..n+1], j <- [0..n+1]]
    cost i j = minimum [k + max (dp ! (i, k-1)) (dp ! (k+1, j)) | k <- [i..j]]
