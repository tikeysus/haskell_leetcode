module Main where

import Solution (combine)

main :: IO ()
main = do
  n <- readLn
  k <- readLn
  print (combine n k)
