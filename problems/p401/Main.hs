module Main where

import Solution (readBinaryWatch)

main :: IO ()
main = readLn >>= print . readBinaryWatch
