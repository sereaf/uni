type Title = String
type Count = Integer

o_O_count :: Title -> Count
o_O_count [] = 0
o_O_count (x:xs)
    | x == 'o' || x == 'O' = 1 + o_O_count xs
    | otherwise = o_O_count xs

longerThan :: [item] -> Count -> Bool
longerThan [] b = False
longerThan (x:xs) 0 = True
longerThan (x:xs) b = longerThan xs (b-1)

merge :: [magic] -> [magic] -> [magic]
merge a [] = a
merge [] b = b
merge (x:xs) (y:ys) = x:y:merge xs ys

starter :: Eq magic => [magic] -> [magic] -> Bool
starter [] [] = True
starter a [] = False
starter [] b = True
starter (x:xs) (y:ys) = x == y && starter xs ys

endings :: [magic] -> [[magic]]
endings [a] = [[a], []]
endings (x:xs) = (x:xs):endings xs