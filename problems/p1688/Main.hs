module Main where

import Solution (numberOfMatches)

main :: IO ()
main = readLn >>= print . numberOfMatches
