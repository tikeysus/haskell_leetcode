module Solution (climbStairs) where

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

climbStairs :: Int -> Integer
climbStairs n = fibs !! (n + 1)
