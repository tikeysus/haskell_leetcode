module Solution (angleClock) where

angleClock :: Int -> Int -> Double
angleClock hour minutes =
  let h = fromIntegral (hour `mod` 12) * 30 + fromIntegral minutes * 0.5
      m = fromIntegral minutes * 6
      d = abs (h - m)
  in min d (360 - d)
