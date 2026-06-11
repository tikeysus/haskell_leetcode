module Solution (countVowelStrings) where

-- C(n+4, 4): non-decreasing strings of length n over 5 vowels
countVowelStrings :: Int -> Int
countVowelStrings n = product [n+1..n+4] `div` 24
