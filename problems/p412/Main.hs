module Main where

import Solution (fizzBuzz)

main :: IO ()
main = interact $ unlines . map (show . fizzBuzz . read) . lines
