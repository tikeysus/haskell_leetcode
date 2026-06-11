module Main where

import Solution (grayCode)

main :: IO ()
main = readLn >>= print . grayCode
