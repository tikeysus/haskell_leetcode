module Main where

import Solution (generate)

main :: IO ()
main = interact $ unlines . map (show . generate . read) . lines
