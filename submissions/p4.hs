module Solution (findMedianSortedArrays) where

import Data.List (sort)

findMedianSortedArrays :: [Int] -> [Int] -> Double
findMedianSortedArrays xs ys =
  let merged = sort (xs ++ ys)
      n      = length merged
  in if odd n
     then fromIntegral (merged !! (n `div` 2))
     else fromIntegral (merged !! (n `div` 2 - 1) + merged !! (n `div` 2)) / 2.0
