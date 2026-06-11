module Main where

import Solution (climbStairs)

main :: IO ()
main = interact $ unlines . map (show . climbStairs . read) . lines
