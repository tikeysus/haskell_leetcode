module Main where

import Solution (simplifiedFractions)

main :: IO ()
main = interact $ unlines . map (show . simplifiedFractions . read) . lines
