module Main where

import Solution (getMoneyAmount)

main :: IO ()
main = interact $ unlines . map (show . getMoneyAmount . read) . lines
