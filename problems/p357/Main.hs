module Main where

import Solution (countNumbersWithUniqueDigits)

main :: IO ()
main = interact $ unlines . map (show . countNumbersWithUniqueDigits . read) . lines
