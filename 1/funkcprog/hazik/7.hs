import Data.List (group)

type Spell magic = (magic -> (Bool, magic))
type Stabilizer magic = (magic -> magic)
type Crate item = [[item]]
type Checker item = (item -> Bool)
type Amount = Int
type Cool = (Amount -> Bool)

prepare :: [Spell container] -> container -> container
prepare [] a = a
prepare (x:xs) a
    | fst (x a) = prepare xs (snd (x a))
    | otherwise = prepare xs a

stabilize :: Eq a => (a -> a) -> a -> a
stabilize f a
    | fa /= a = stabilize f fa
    | otherwise = a 
    where
        fa = f a 

brew :: (Integral a, Num b) => (b -> Bool) -> (b -> b) -> [[a]] -> b
brew p f l = sum [if p $ fromIntegral x then fromIntegral x else f $ fromIntegral x  | x <- map sum l]

cooldown :: Eq a => [a] -> (Int -> Bool) -> [a]
cooldown l p = concat [if p $ length x then [head x] else x  | x <- group l]