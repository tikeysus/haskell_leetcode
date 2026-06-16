module Solution (generateMatrix) where

generateMatrix :: Int -> [[Int]]
generateMatrix n = place (spiralCoords n) 1 (replicate n (replicate n 0))
  where
    place [] _ g = g
    place ((r,c):rest) v g =
      let row  = g !! r
          row' = take c row ++ [v] ++ drop (c+1) row
          g'   = take r g ++ [row'] ++ drop (r+1) g
      in place rest (v+1) g'

    spiralCoords m = go 0 (m-1) 0 (m-1)
    go rl rh cl ch
      | rl > rh || cl > ch = []
      | rl == rh            = [(rl, c) | c <- [cl..ch]]
      | cl == ch            = [(r, cl) | r <- [rl..rh]]
      | otherwise           =
          [(rl, c) | c <- [cl..ch]]            ++
          [(r, ch) | r <- [rl+1..rh]]          ++
          [(rh, c) | c <- [ch-1,ch-2..cl]]     ++
          [(r, cl) | r <- [rh-1,rh-2..rl+1]]  ++
          go (rl+1) (rh-1) (cl+1) (ch-1)
