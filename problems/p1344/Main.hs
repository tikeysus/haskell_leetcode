module Main where

import Solution (angleClock)
import Text.Printf (printf)

main :: IO ()
main = do
  hour    <- readLn
  minutes <- readLn
  printf "%.5f\n" (angleClock hour minutes)
