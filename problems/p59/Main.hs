module Main where

import Solution (generateMatrix)

main :: IO ()
main = interact $ unlines . map (show . generateMatrix . read) . lines
