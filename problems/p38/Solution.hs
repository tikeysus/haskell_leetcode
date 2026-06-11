module Solution (countAndSay) where

countAndSay :: Int -> String
countAndSay = (iterate say "1" !!) . subtract 1
  where
    say        = concatMap encode . group
    encode g   = show (length g) ++ [head g]
    group []     = []
    group (x:xs) = let (same, rest) = span (== x) xs
                   in (x : same) : group rest
