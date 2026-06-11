module Main where

import Solution (numsSameConsecDiff)

main :: IO ()
main = do
  n <- readLn
  k <- readLn
  print (numsSameConsecDiff n k)
