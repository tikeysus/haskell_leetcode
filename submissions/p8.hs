module Solution (myAtoi) where

import Data.Char (isDigit, isSpace)

myAtoi :: String -> Int
myAtoi s =
  let s1         = dropWhile isSpace s
      (sign, s2) = case s1 of
                     ('+':rest) -> ( 1, rest)
                     ('-':rest) -> (-1, rest)
                     _          -> ( 1, s1)
      digits     = takeWhile isDigit s2
      n          = if null digits then 0 else sign * (read digits :: Integer)
  in fromIntegral (max (-2147483648) (min 2147483647 n))
