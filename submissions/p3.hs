module Solution (lengthOfLongestSubstring) where

import Data.List (elemIndex)

lengthOfLongestSubstring :: String -> Int
lengthOfLongestSubstring = snd . foldl step ([], 0)
  where
    step (win, best) c = case elemIndex c win of
      Nothing -> (win ++ [c], max best (length win + 1))
      Just i  -> let win' = drop (i + 1) win ++ [c]
                 in (win', max best (length win'))
