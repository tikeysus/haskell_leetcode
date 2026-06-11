module Main where

import Solution (letterCombinations)

main :: IO ()
main = interact $ unlines . map (show . letterCombinations) . lines
