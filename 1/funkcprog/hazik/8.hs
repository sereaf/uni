newtype Table = T String deriving (Show, Eq)

to_table :: String -> Table
to_table = T

change :: Table -> String -> Table
change (T _) = T

data Dummy = Alive Int | Dead deriving (Show, Eq)

updateHealth :: Dummy -> Int -> Dummy
updateHealth (Alive h) d
    | h <= d = Dead
    | otherwise = Alive (h-d)
updateHealth d _ = Dead

multi_hit :: [Dummy] -> Int -> [Dummy]
multi_hit l d = [updateHealth x d | x <- l]

megahit :: [Dummy] -> Int -> [Dummy]
megahit [] _ = []
megahit (Alive h:xs) d
    | updateHealth (Alive h) d == Dead = Dead:megahit xs (d-h)
    | otherwise = updateHealth (Alive h) d:xs
