module Solution (fib) where

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

fib :: Int -> Integer
fib = (fibs !!)
