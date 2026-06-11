module Solution (validStrings) where

validStrings :: Int -> [String]
validStrings n = go n '1'
  where
    go 0 _    = [""]
    go k prev =
      ['1' : s | s <- go (k-1) '1'] ++
      ['0' : s | prev == '1', s <- go (k-1) '0']
