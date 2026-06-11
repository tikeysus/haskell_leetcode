module Solution (getMaximumGenerated) where

getMaximumGenerated :: Int -> Int
getMaximumGenerated 0 = 0
getMaximumGenerated n = maximum nums
  where
    nums  = take (n + 1) gen
    gen   = 0 : 1 : [f i | i <- [2..n]]
    f i   = if even i then gen !! (i `div` 2)
                      else gen !! (i `div` 2) + gen !! (i `div` 2 + 1)
