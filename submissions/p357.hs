module Solution (countNumbersWithUniqueDigits) where

countNumbersWithUniqueDigits :: Int -> Int
countNumbersWithUniqueDigits 0 = 1
countNumbersWithUniqueDigits n = 10 + sum (tail (take n (scanl (*) 9 [9,8..])))
