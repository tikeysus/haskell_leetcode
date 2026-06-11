module Solution (tribonacci) where

tribs :: [Integer]
tribs = 0 : 1 : 1 : zipWith3 (\a b c -> a + b + c) tribs (tail tribs) (tail (tail tribs))

tribonacci :: Int -> Integer
tribonacci = (tribs !!)
