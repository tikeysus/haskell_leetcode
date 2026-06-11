module Main where

import Solution (numPrimeArrangements)

main :: IO ()
main = readLn >>= print . numPrimeArrangements
