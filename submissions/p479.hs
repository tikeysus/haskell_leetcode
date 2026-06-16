module Solution (largestPalindrome) where

largestPalindrome :: Int -> Int
largestPalindrome 1 = 9
largestPalindrome n = fromInteger $ head
  [ p `mod` 1337
  | t <- [hi, hi-1..lo]
  , let p = mkPal t
  , p <= hi * hi
  , any (\a -> p `mod` a == 0 && p `div` a >= lo && p `div` a <= hi)
        [min hi (p `div` lo), min hi (p `div` lo) - 1 .. isqrt p]
  ]
  where
    hi  = 10^n - 1 :: Integer
    lo  = 10^(n-1) :: Integer
    mkPal t = let s = show t in read (s ++ reverse s) :: Integer
    isqrt x = let s = floor (sqrt (fromIntegral x :: Double)) :: Integer
              in if (s+1)*(s+1) <= x then s+1 else s
