module Main where

import Solution (numTrees)

main :: IO ()
main = interact $ unlines . map (show . numTrees . read) . lines
