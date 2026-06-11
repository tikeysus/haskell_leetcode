module Main where

import Solution (longestPalindrome)

main :: IO ()
main = getLine >>= putStrLn . longestPalindrome
