module Solution (simplifiedFractions) where

simplifiedFractions :: Int -> [String]
simplifiedFractions n =
  [ show a ++ "/" ++ show b
  | b <- [2..n]
  , a <- [1..b-1]
  , gcd a b == 1
  ]
