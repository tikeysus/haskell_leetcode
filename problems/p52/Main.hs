module Main where

import Solution (totalNQueens)

main :: IO ()
main = interact $ unlines . map (show . totalNQueens . read) . lines
