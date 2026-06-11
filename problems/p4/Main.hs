module Main where

import Solution (findMedianSortedArrays)
import Text.Printf (printf)

main :: IO ()
main = do
  nums1 <- fmap (read :: String -> [Int]) getLine
  nums2 <- fmap (read :: String -> [Int]) getLine
  printf "%.5f\n" (findMedianSortedArrays nums1 nums2)
