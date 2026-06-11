module Solution (divide) where

divide :: Int -> Int -> Int
divide dividend divisor =
  max (-2147483648) (min 2147483647 (quot dividend divisor))
