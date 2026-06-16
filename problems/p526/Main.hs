module Main where

import Solution (countArrangement)

main :: IO ()
main = interact $ unlines . map (show . countArrangement . read) . lines
