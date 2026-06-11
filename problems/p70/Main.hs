module Main where

import Solution (climbStairs)

main :: IO ()
main = readLn >>= print . climbStairs
