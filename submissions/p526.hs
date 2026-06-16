module Solution (countArrangement) where

countArrangement :: Int -> Int
countArrangement n = go 1 [1..n]
  where
    go pos []    = 1
    go pos avail = sum
      [ go (pos + 1) (filter (/= x) avail)
      | x <- avail
      , pos `mod` x == 0 || x `mod` pos == 0
      ]
