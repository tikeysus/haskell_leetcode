module Main where

import Solution (myAtoi)

main :: IO ()
main = getLine >>= print . myAtoi
