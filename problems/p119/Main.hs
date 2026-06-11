module Main where

import Solution (getRow)

main :: IO ()
main = interact $ unlines . map (show . getRow . read) . lines
