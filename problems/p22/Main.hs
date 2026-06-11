module Main where

import Solution (generateParenthesis)

main :: IO ()
main = readLn >>= print . generateParenthesis
