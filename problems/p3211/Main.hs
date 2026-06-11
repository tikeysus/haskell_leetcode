module Main where

import Solution (validStrings)

main :: IO ()
main = interact $ unlines . map (show . validStrings . read) . lines
