module Main where

import Solution (countVowelStrings)

main :: IO ()
main = readLn >>= print . countVowelStrings
