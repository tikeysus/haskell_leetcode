module Main where

import Solution (countVowelStrings)

main :: IO ()
main = interact $ unlines . map (show . countVowelStrings . read) . lines
