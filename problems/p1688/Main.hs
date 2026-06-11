module Main where

import Solution (numberOfMatches)

main :: IO ()
main = interact $ unlines . map (show . numberOfMatches . read) . lines
