module Solution (intToRoman) where

intToRoman :: Int -> String
intToRoman n = go n table
  where
    table = [ (1000,"M"),(900,"CM"),(500,"D"),(400,"CD")
            , (100,"C"),(90,"XC"),(50,"L"),(40,"XL")
            , (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I") ]
    go 0 _              = ""
    go _ []             = ""
    go x ((v,s):rest)   = concat (replicate q s) ++ go r rest
      where (q, r) = x `divMod` v
