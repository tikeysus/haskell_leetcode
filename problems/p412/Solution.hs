module Solution (fizzBuzz) where

fizzBuzz :: Int -> [String]
fizzBuzz n = map f [1..n]
  where
    f i | i `mod` 15 == 0 = "FizzBuzz"
        | i `mod` 3  == 0 = "Fizz"
        | i `mod` 5  == 0 = "Buzz"
        | otherwise        = show i
