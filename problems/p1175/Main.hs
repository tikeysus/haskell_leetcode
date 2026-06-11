module Main where

import Solution (numPrimeArrangements)

main :: IO ()
main = interact $ unlines . map (show . numPrimeArrangements . read) . lines
