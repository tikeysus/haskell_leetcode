module Solution (Tree(..), allPossibleFBT) where

data Tree a = Leaf | Node (Tree a) a (Tree a)

allPossibleFBT :: Int -> [Tree Int]
allPossibleFBT 1 = [Node Leaf 0 Leaf]
allPossibleFBT n
  | even n    = []
  | otherwise = [ Node l 0 r
                | i <- [1,3..n-2]
                , l <- allPossibleFBT i
                , r <- allPossibleFBT (n - 1 - i)
                ]
