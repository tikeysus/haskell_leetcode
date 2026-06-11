module Solution (letterCombinations) where

letterCombinations :: String -> [String]
letterCombinations [] = []
letterCombinations ds = foldr1 combine (map letters ds)
  where
    letters '2' = ["a","b","c"]
    letters '3' = ["d","e","f"]
    letters '4' = ["g","h","i"]
    letters '5' = ["j","k","l"]
    letters '6' = ["m","n","o"]
    letters '7' = ["p","q","r","s"]
    letters '8' = ["t","u","v"]
    letters '9' = ["w","x","y","z"]
    letters _   = []
    combine xs ys = [x ++ y | x <- xs, y <- ys]
