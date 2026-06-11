module Main where

import Solution (getMaximumGenerated)

main :: IO ()
main = readLn >>= print . getMaximumGenerated
