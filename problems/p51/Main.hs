module Main where

import Solution (solveNQueens)

main :: IO ()
main = readLn >>= print . solveNQueens
