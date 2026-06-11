module Main where

import Solution (tribonacci)

main :: IO ()
main = interact $ unlines . map (show . tribonacci . read) . lines
