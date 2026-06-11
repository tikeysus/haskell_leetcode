module Solution (Tree(..), generateTrees) where

data Tree a = Leaf | Node (Tree a) a (Tree a)

generateTrees :: Int -> [Tree Int]
generateTrees n = go 1 n
  where
    go lo hi
      | lo > hi   = [Leaf]
      | otherwise = [ Node l i r
                    | i <- [lo..hi]
                    , l <- go lo (i - 1)
                    , r <- go (i + 1) hi
                    ]
