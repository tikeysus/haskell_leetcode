module Solution (numberOfChild) where

numberOfChild :: Int -> Int -> Int
numberOfChild n k = let period = 2 * (n - 1)
                        pos    = k `mod` period
                    in if pos <= n - 1 then pos else period - pos
