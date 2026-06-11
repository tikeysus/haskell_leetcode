module Main where

import Solution (sumOfTheDigitsOfHarshadNumber)

main :: IO ()
main = readLn >>= print . sumOfTheDigitsOfHarshadNumber
