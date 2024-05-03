import Data.List (group)

type Room = String
type Air = Int
type Fire = Integer
type MagicLevel = Int

find :: [Room] -> [Room]
find l = [x | x <- l, x =="2.620"]

add :: (Integral magic1, Integral magic2, Num magic3) => magic1 -> magic2 -> magic3
add a b = fromIntegral a + fromIntegral b

prime_magic :: MagicLevel -> MagicLevel -> [MagicLevel]
prime_magic a b = [x | x <- [a..b], isPrime x]

isPrime :: Integral a => a -> Bool
isPrime k = length [ x | x <- [2..k], k `mod` x == 0] == 1

compress :: Eq magic => [magic] -> [(magic, MagicLevel)]
compress a =  [(head x, length x) | x <-  group a]

decompress :: Eq magic => [(magic, MagicLevel)] -> [magic]
decompress a =  [fst x | x <- a, y <- [1..snd x]]


