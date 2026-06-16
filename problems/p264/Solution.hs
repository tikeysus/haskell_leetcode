module Solution (nthUglyNumber) where

nthUglyNumber :: Int -> Int
nthUglyNumber n = ugly !! (n - 1)
  where
    ugly = 1 : merge3 (map (2*) ugly) (map (3*) ugly) (map (5*) ugly)

merge3 :: [Int] -> [Int] -> [Int] -> [Int]
merge3 (x:xs) (y:ys) (z:zs)
  | x <= y && x <= z = x : merge3 xs (dropEq x y ys) (dropEq x z zs)
  | y <= z           = y : merge3 (x:xs) ys (dropEq y z zs)
  | otherwise        = z : merge3 (x:xs) (y:ys) zs
  where dropEq a b bs = if a == b then bs else b:bs
merge3 _ _ _ = []
