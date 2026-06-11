module Main where

import Solution (myAtoi)

main :: IO ()
main = interact $ unlines . map (show . myAtoi) . lines
