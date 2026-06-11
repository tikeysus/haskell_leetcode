module Solution (countTriples) where

countTriples :: Int -> Int
countTriples n = length
  [ ()
  | a <- [1..n], b <- [1..n]
  , let c2 = a*a + b*b
  , c2 <= n*n
  , let c = floor (sqrt (fromIntegral c2 :: Double))
  , c*c == c2
  ]
