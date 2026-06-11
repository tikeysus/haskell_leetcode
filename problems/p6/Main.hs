module Main where

import Solution (convert)

main :: IO ()
main = do
  s       <- getLine
  numRows <- readLn
  putStrLn (convert s numRows)
