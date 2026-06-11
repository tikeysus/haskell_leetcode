module Main where

import Solution (totalNQueens)

main :: IO ()
main = readLn >>= print . totalNQueens
