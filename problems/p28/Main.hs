module Main where

import Solution (strStr)

chunksOf :: Int -> [a] -> [[a]]
chunksOf _ [] = []
chunksOf n xs = take n xs : chunksOf n (drop n xs)

main :: IO ()
main = do
  ls <- lines <$> getContents
  mapM_ (\[l1,l2] -> print (strStr l1 l2)) (chunksOf 2 ls)
