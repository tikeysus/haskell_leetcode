module Main where

import Solution (twoSum)

main :: IO ()
main = do
  nums   <- fmap (read :: String -> [Int]) getLine
  target <- readLn
  print (twoSum nums target)
