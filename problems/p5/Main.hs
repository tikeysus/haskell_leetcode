module Main where

import Solution (longestPalindrome)

main :: IO ()
main = interact $ unlines . map longestPalindrome . lines
