module Solution (twoSum) where

twoSum :: [Int] -> Int -> [Int]
twoSum nums target =
  head [ [i, j] | (i, x) <- zip [0..] nums
                , (j, y) <- zip [0..] nums
                , i < j, x + y == target ]
