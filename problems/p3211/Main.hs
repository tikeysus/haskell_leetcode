module Main where

import Solution (validStrings)

main :: IO ()
main = readLn >>= print . validStrings
