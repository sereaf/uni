module LastHomework  where
import Data.Char (toUpper)

which :: ([Char], [Char], [Char]) -> Char -> Int
which (a, b, c) ch
    | not $ all (\d -> d == False) $ map (\d -> d == ch) a = 1
    | not $ all (\d -> d == False) $ map (\d -> d == ch) b = 2
    | not $ all (\d -> d == False) $ map (\d -> d == ch) c = 3
    | otherwise = 0

matches :: (Int, Int) -> (Int, Int) -> Bool
matches (a, b) (c, d) = b == c

toUpperCase :: String -> String
toUpperCase [] = []
toUpperCase (ch:chs) = toUpper ch : chs

swap :: Maybe a -> b -> Maybe b
swap Nothing _ = Nothing
swap (Just a) b = Just b

numeric :: String -> Int
numeric [] = 0
numeric (x:xs)
    | x == 'r' = 4 + numeric xs
    | x == 'w' = 2 + numeric xs
    | x == 'x' = 1 + numeric xs

pythagoreans :: [(Int, Int, Int)]
pythagoreans = [(a, b, c) | a <- [0..100], b <- [0..100], c <- [0..100], a*a + b*b == c*c, b > a && c > b]

hasLongWord :: Int -> String -> Bool
hasLongWord n s = any (\a -> length a >= n) (words s)

align :: Int -> String -> String
align n s
    | n <= 0 = s
    | length s < n = align n (" " ++ s)
    | otherwise = s

modify :: (a -> Maybe a) -> [a] -> [a]
modify f [] = []
modify f l@(x:xs)
    | Nothing <- nx = xs
    | (Just a) <- nx = a:xs where
        nx = f x

isLonger :: [a] -> Int -> Bool
isLonger l n = length (take (n+1) l) > n

acc :: [(Char, Int)]
acc = zip ['á', 'é', 'í', 'ó', 'ö', 'ő', 'ú', 'ű', 'ü'] [0..]
racc :: [(Char, Int)]
racc = zip ['a', 'e', 'i', 'o', 'o', 'o', 'u', 'u', 'u'] [0..]
removeAccents :: String -> String
removeAccents [] = []
removeAccents (ch:chs) =  (if not (null rch) then head rch else ch):removeAccents chs where
    rch = [y | (x, i) <- acc, x == ch, (y, j) <- racc, i == j]

strip :: String -> String
strip [] = []
strip s = dropWhile (=='_') $ reverse (dropWhile (=='_') (reverse s))

data RPS = Rock | Paper | Scissors deriving Eq

beats :: RPS -> RPS
beats Paper = Rock
beats Rock = Scissors
beats Scissors = Paper

firstBeats :: [RPS] -> [RPS] -> Int
firstBeats [] [] = 0
firstBeats (x:xs) (y:ys)
    | y == beats x = 1 + firstBeats xs ys
    | otherwise = firstBeats xs ys

data Temperature = Daytime Int | Night Int deriving Eq

isDaytime :: Temperature -> Bool
isDaytime (Daytime a) = True
isDaytime _ = False

extremes :: [Temperature] -> (Int, Int)
extremes l = (maximum [x | (Daytime x) <- l], minimum [x | (Night x) <- l])