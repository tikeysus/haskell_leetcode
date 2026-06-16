module Main where

import Solution (intToRoman)

main :: IO ()
main = interact $ unlines . map (intToRoman . read) . lines
