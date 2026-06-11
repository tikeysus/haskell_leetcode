module Main where

import Solution (simplifiedFractions)

main :: IO ()
main = readLn >>= print . simplifiedFractions
