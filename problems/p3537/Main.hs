module Main where

import Solution (specialGrid)

main :: IO ()
main = interact $ unlines . map (show . specialGrid . read) . lines
