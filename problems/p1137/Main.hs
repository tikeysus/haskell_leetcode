module Main where

import Solution (tribonacci)

main :: IO ()
main = readLn >>= print . tribonacci
