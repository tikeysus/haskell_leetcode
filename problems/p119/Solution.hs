module Solution (getRow) where

getRow :: Int -> [Int]
getRow n = rows !! n
  where
    rows = [1] : map nextRow rows
    nextRow r = zipWith (+) (0 : r) (r ++ [0])
