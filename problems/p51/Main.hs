module Main where

import Solution (solveNQueens)

main :: IO ()
main = interact $ unlines . map (show . solveNQueens . read) . lines
