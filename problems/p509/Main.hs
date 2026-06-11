module Main where

import Solution (fib)

main :: IO ()
main = interact $ unlines . map (show . fib . read) . lines
