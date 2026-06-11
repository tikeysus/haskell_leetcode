module Main where

import Solution (strStr)

main :: IO ()
main = do
  haystack <- getLine
  needle   <- getLine
  print (strStr haystack needle)
