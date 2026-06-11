module Main where

import Solution (lengthOfLongestSubstring)

main :: IO ()
main = interact $ unlines . map (show . lengthOfLongestSubstring) . lines
