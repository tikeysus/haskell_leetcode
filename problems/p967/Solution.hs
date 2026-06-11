module Solution (numsSameConsecDiff) where

numsSameConsecDiff :: Int -> Int -> [Int]
numsSameConsecDiff n k
  | n == 1    = [0..9]
  | otherwise = concatMap extend [1..9]
  where
    extend d = go (n - 1) d d
    go 0 _ acc = [acc]
    go r last_ acc =
      let next d = go (r-1) d (acc * 10 + d)
          hi = last_ + k
          lo = last_ - k
      in (if hi <= 9 then next hi else []) ++
         (if k /= 0 && lo >= 0 then next lo else [])
