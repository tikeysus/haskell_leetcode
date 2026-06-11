module Solution (sumOfTheDigitsOfHarshadNumber) where

sumOfTheDigitsOfHarshadNumber :: Int -> Int
sumOfTheDigitsOfHarshadNumber x =
  let s = sum [ fromEnum c - fromEnum '0' | c <- show x ]
  in if x `mod` s == 0 then x else -1
