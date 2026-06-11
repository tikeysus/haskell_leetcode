module Main where

import Solution (countAndSay)

main :: IO ()
main = interact $ unlines . map (countAndSay . read) . lines
