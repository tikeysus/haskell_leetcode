module Main where

import Solution (countTriples)

main :: IO ()
main = interact $ unlines . map (show . countTriples . read) . lines
