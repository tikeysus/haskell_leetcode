module Main where

import Solution (combine)

chunksOf :: Int -> [a] -> [[a]]
chunksOf _ [] = []
chunksOf n xs = take n xs : chunksOf n (drop n xs)

main :: IO ()
main = do
  ls <- lines <$> getContents
  mapM_ (\[l1,l2] -> print (combine (read l1 :: Int) (read l2 :: Int))) (chunksOf 2 ls)
