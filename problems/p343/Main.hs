module Main where

import Solution (integerBreak)

main :: IO ()
main = interact $ unlines . map (show . integerBreak . read) . lines
