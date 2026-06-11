module Solution (readBinaryWatch) where

import Data.Bits (popCount)

readBinaryWatch :: Int -> [String]
readBinaryWatch turnedOn =
  [ show h ++ ":" ++ (if m < 10 then "0" else "") ++ show m
  | h <- [0..11 :: Int]
  , m <- [0..59 :: Int]
  , popCount h + popCount m == turnedOn
  ]
