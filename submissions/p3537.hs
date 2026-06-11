module Solution (specialGrid) where

specialGrid :: Int -> [[Int]]
specialGrid n = build (1 `shiftL` n) 0
  where
    shiftL x k = x * (2 ^ k)
    build 1 start = [[start]]
    build size start =
      let half    = size `div` 2
          quarter = half * half
          tr = build half start
          br = build half (start + quarter)
          bl = build half (start + 2 * quarter)
          tl = build half (start + 3 * quarter)
      in zipWith (++) tl tr ++ zipWith (++) bl br
