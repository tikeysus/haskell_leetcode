module Main where

import Solution (numSquares)

main :: IO ()
main = interact $ unlines . map (show . numSquares . read) . lines
