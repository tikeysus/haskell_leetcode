module Solution (largestPalindrome) where

largestPalindrome :: Int -> Int
largestPalindrome 1 = 9
largestPalindrome n =
  let upper = 10 ^ n - 1 :: Integer
      lower = 10 ^ (n - 1) :: Integer
      mkPal a = let s = show a in read (s ++ reverse s) :: Integer
      isDivisible p = any (\b -> p `mod` b == 0 && p `div` b >= lower)
                          [upper, upper - 1 .. ceiling (sqrt (fromIntegral p :: Double))]
  in fromIntegral (head (filter isDivisible (map mkPal [upper, upper - 1 .. lower]))) `mod` 1337
