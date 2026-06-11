module Main where

import Solution (generateParenthesis)

main :: IO ()
main = interact $ unlines . map (show . generateParenthesis . read) . lines
