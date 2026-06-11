module Main where

import Solution (readBinaryWatch)

main :: IO ()
main = interact $ unlines . map (show . readBinaryWatch . read) . lines
