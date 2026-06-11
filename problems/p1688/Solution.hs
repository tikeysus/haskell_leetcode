module Solution (numberOfMatches) where

-- Every match eliminates exactly one team; n-1 eliminations needed.
numberOfMatches :: Int -> Int
numberOfMatches n = n - 1
