module Solution (countGoodIntegers) where

import Data.List (sort, group)

countGoodIntegers :: Int -> Int -> Integer
countGoodIntegers n k =
  let half  = (n + 1) `div` 2
      lo    = 10 ^ (half - 1) :: Integer
      hi    = 10 ^ half - 1   :: Integer
      pals  = [ p | s <- [lo..hi]
                  , let p = makePalindrome n s
                  , p `mod` fromIntegral k == 0 ]
      msets = map head . group . sort $ map (sort . show) pals
  in sum $ map (countPerms n) msets

makePalindrome :: Int -> Integer -> Integer
makePalindrome n prefix =
  let s   = show prefix
      pal = if odd n then s ++ reverse (init s) else s ++ reverse s
  in read pal

countPerms :: Int -> String -> Integer
countPerms n digits =
  let total    = fac n `div` product (map (fac . length) (group digits))
      without0 = if '0' `elem` digits
                 then fac (n-1) `div` product (map (fac . length) (group (drop1 '0' digits)))
                 else 0
  in total - without0

drop1 :: Eq a => a -> [a] -> [a]
drop1 _ []     = []
drop1 x (y:ys) = if x == y then ys else y : drop1 x ys

fac :: Int -> Integer
fac 0 = 1
fac m = fromIntegral m * fac (m - 1)
