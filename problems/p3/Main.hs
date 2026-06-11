module Main where

import Solution (lengthOfLongestSubstring)

main :: IO ()
main = getLine >>= print . lengthOfLongestSubstring
