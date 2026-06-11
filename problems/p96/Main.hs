module Main where

import Solution (numTrees)

main :: IO ()
main = readLn >>= print . numTrees
