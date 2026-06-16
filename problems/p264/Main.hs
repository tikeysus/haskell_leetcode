module Main where

import Solution (nthUglyNumber)

main :: IO ()
main = interact $ unlines . map (show . nthUglyNumber . read) . lines
