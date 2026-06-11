module Main where

import Solution (Tree(..), allPossibleFBT)
import Data.List (intercalate)

serialize :: Tree Int -> String
serialize t = "[" ++ intercalate "," (map showNode (trimNulls (levelOrder [t]))) ++ "]"
  where
    showNode Nothing  = "null"
    showNode (Just x) = show x
    trimNulls = reverse . dropWhile (== Nothing) . reverse
    levelOrder []                  = []
    levelOrder (Leaf       : rest) = Nothing : levelOrder rest
    levelOrder (Node l v r : rest) = Just v  : levelOrder (rest ++ [l, r])

main :: IO ()
main = interact $ unlines . map (serializeTrees . allPossibleFBT . read) . lines
  where serializeTrees ts = "[" ++ intercalate "," (map serialize ts) ++ "]"
