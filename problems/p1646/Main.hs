module Main where

import Solution (getMaximumGenerated)

main :: IO ()
main = interact $ unlines . map (show . getMaximumGenerated . read) . lines
