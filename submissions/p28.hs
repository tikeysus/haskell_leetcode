module Solution (strStr) where

import Data.List (isPrefixOf)

strStr :: String -> String -> Int
strStr haystack needle
  | null needle = 0
  | otherwise   = go 0 haystack
  where
    go _ []       = -1
    go i hs@(_:t)
      | needle `isPrefixOf` hs = i
      | otherwise               = go (i + 1) t
