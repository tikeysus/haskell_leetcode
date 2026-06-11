module Main where

import Solution (generate)

main :: IO ()
main = readLn >>= print . generate
