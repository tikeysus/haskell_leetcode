module Solution (kthCharacter) where

kthCharacter :: Int -> Char
kthCharacter k = toChar $ digits !! (k - 1)
  where
    toChar n = toEnum (fromEnum 'a' + n)
    digits   = go [0]
    go xs
      | length xs >= k = xs
      | otherwise      = go (xs ++ map (\c -> (c + 1) `mod` 26) xs)
