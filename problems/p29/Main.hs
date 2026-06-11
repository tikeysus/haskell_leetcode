module Main where

import Solution (divide)

main :: IO ()
main = do
  dividend <- readLn
  divisor  <- readLn
  print (divide dividend divisor)
