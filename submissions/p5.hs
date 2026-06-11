module Solution (longestPalindrome) where

longestPalindrome :: String -> String
longestPalindrome "" = ""
longestPalindrome s  = foldl1 longer candidates
  where
    n = length s
    expand l r
      | l < 0 || r >= n || s !! l /= s !! r = take (r - l - 1) (drop (l + 1) s)
      | otherwise                             = expand (l - 1) (r + 1)
    candidates = [expand i i       | i <- [0 .. n - 1]]
              ++ [expand i (i + 1) | i <- [0 .. n - 2]]
    longer a b = if length b > length a then b else a
