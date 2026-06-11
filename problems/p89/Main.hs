module Main where

import Solution (grayCode)

main :: IO ()
main = interact $ unlines . map (show . grayCode . read) . lines
