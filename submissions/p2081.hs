module Solution (kMirror) where

kMirror :: Int -> Int -> Integer
kMirror k n = sum $ take n $ filter (isPalBase k) decimalPalindromes

decimalPalindromes :: [Integer]
decimalPalindromes = concatMap palindromesOfLength [1..]
  where
    palindromesOfLength len =
      let half   = (len + 1) `div` 2
          start  = 10 ^ (half - 1)
          end    = 10 ^ half - 1
      in [ buildPal p len | p <- [start..end] ]
    buildPal prefix len =
      let s    = show prefix
          rev  = reverse s
          tail = if even len then rev else tail' rev
          tail' (_:xs) = xs
          tail' []     = []
      in read (s ++ tail)

isPalBase :: Int -> Integer -> Bool
isPalBase base n = ds == reverse ds
  where
    ds = toBaseDigits (fromIntegral base) n

toBaseDigits :: Integer -> Integer -> [Integer]
toBaseDigits _    0 = [0]
toBaseDigits base n = reverse (go n)
  where
    go 0 = []
    go x = (x `mod` base) : go (x `div` base)
