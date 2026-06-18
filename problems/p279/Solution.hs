module Solution (numSquares) where

numSquares :: Int -> Int
numSquares n
  | isSquare n                                    = 1
  | is4Form n                                     = 4
  | any (\j -> isSquare (n - j*j)) [1..isqrt n]  = 2
  | otherwise                                     = 3
  where
    isqrt x   = let s = floor (sqrt (fromIntegral x :: Double))
                in if (s+1)*(s+1) == x then s+1 else s
    isSquare x = let s = isqrt x in s*s == x
    is4Form x
      | x `mod` 4 == 0 = is4Form (x `div` 4)
      | otherwise       = x `mod` 8 == 7
