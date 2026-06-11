module Main where

import Solution (countAndSay)

main :: IO ()
main = readLn >>= putStrLn . countAndSay
