module Solution (numTrees) where

catalan :: [Int]
catalan = 1 : [sum [catalan !! i * catalan !! (k - 1 - i) | i <- [0..k-1]] | k <- [1..]]

numTrees :: Int -> Int
numTrees = (catalan !!)
