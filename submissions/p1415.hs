module Solution (getHappyString) where

getHappyString :: Int -> Int -> String
getHappyString n k =
  let strings = go "" n
  in if k > length strings then "" else strings !! (k - 1)
  where
    go curr 0 = [curr]
    go curr m = concatMap (\c -> if null curr || last curr /= c
                                 then go (curr ++ [c]) (m - 1)
                                 else []) "abc"
