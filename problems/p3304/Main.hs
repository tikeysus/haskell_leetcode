module Main where

import Solution (kthCharacter)

main :: IO ()
main = interact $ unlines . map ((:[]) . kthCharacter . read) . lines
