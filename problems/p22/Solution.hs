module Solution (generateParenthesis) where

generateParenthesis :: Int -> [String]
generateParenthesis n = go 0 0 ""
  where
    go open close curr
      | length curr == 2 * n = [curr]
      | otherwise =
          (if open  < n    then go (open+1) close   (curr ++ "(") else []) ++
          (if close < open then go open    (close+1) (curr ++ ")") else [])
