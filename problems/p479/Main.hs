module Main where

import Solution (largestPalindrome)

main :: IO ()
main = interact $ unlines . map (show . largestPalindrome . read) . lines
