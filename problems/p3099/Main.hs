module Main where

import Solution (sumOfTheDigitsOfHarshadNumber)

main :: IO ()
main = interact $ unlines . map (show . sumOfTheDigitsOfHarshadNumber . read) . lines
