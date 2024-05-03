type Air = Int
type Fire = Integer
type Shadow = Float
type Haskell = Double
type Open = String
type Key a b = [[(a,[b])]]
type Type = String
type Power = Integer
type Missile = (Type, Power)

mind_vision :: Ord magic => [magic] -> Bool
mind_vision [] = True
mind_vision [a] = True
mind_vision (x:y:xs)
    | x < y = mind_vision (y:xs)
    | otherwise = False

lock :: Key a b -> Open
lock [(x,xs):[y,ys]]            = "First"
lock ([_]:[(x,[xs])]:[y,ys]:[]) = "Second"
lock ([(x,y:_:[])]:[])          = "Third"

magic_key_1 = [[(1, []), (1, []), (1, [])]]
magic_key_2 = [[(1, [])],[(1,[2])],[(1, [1]), (1, [1])]]
magic_key_3 = [[(1, [1, 1])]]

mage_armor :: [Missile] -> Type -> Power
mage_armor [] _ = 0
mage_armor ((x ,y):xs) b
    | x /= b = y + mage_armor xs b
    | otherwise = mage_armor xs b

backfire :: [Missile] -> [Missile]
backfire [] = []  
backfire [a]
    | snd a >= 50 = [a]
    | otherwise = [] 
backfire ((x, y):xs) 
    |  y < 50 = backfire [if a == x then (a, b-y) else (a, b) | (a, b) <- xs]
    | otherwise = (x, y):backfire xs

{- ([(a, b-y) | (a, b) <- xs, a == x] ++ [(a, b) | (a, b) <- xs, a /= x]) -}