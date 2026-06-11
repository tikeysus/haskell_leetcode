module Main where

import Solution (fib)

main :: IO ()
main = readLn >>= print . fib
