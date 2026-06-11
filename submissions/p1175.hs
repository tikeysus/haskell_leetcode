module Solution (numPrimeArrangements) where

numPrimeArrangements :: Int -> Int
numPrimeArrangements n =
  let p = length (filter isPrime [2..n])
      m = 1000000007
  in fromInteger (modFac p m * modFac (n - p) m `mod` fromIntegral m)
  where
    isPrime x = x >= 2 && all (\i -> x `mod` i /= 0) [2..floor (sqrt (fromIntegral x :: Double))]
    modFac 0 _ = 1
    modFac k m = fromIntegral k * modFac (k-1) m `mod` m
