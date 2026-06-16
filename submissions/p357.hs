module Solution (countNumbersWithUniqueDigits) where

countNumbersWithUniqueDigits :: Int -> Int
countNumbersWithUniqueDigits 0 = 1
countNumbersWithUniqueDigits n =
  countNumbersWithUniqueDigits (n-1) + 9 * product (take (n-1) [9,8..1])
