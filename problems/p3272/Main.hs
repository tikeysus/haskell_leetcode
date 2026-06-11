module Main where

import Solution (countGoodIntegers)

main :: IO ()
main = do
  n <- readLn
  k <- readLn
  print (countGoodIntegers n k)
