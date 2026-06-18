module Main where

import Solution (trailingZeroes)

main :: IO ()
main = interact $ unlines . map (show . trailingZeroes . read) . lines
