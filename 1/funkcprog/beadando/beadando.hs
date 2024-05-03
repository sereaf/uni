showState a = show a
showMage a = show a
eqMage a b = a == b
showUnit a = show a
showOneVOne a = show a

type Name = String
type Health = Integer
type Spell = (Integer -> Integer)
type Army = [Unit]
type EnemyArmy = Army
type Amount = Integer

data State a = Alive a | Dead deriving (Eq)
instance Show a => Show (State a) where
    show (Alive a) = show a
    show Dead =  "Dead"

data Entity = Golem Health | HaskellElemental Health deriving (Show, Eq)

data Mage = Master Name Health Spell
instance Show Mage where
    show (Master a b c)
        | b < 5 = "Wounded " ++ a
        | otherwise = a
instance Eq Mage where
    (Master a b c) == (Master d e f) = a == d && b == e

papi = let
    tunderpor enemyHP
        | enemyHP < 8 = 0
        | even enemyHP = div (enemyHP * 3) 4
        | otherwise = enemyHP - 3
    in Master "Papi" 126 tunderpor
java = Master "Java" 100 (\x ->  x - mod x 9)
traktor = Master "Traktor" 20 (\x -> div (x + 10) (mod x 4 + 1))
jani = Master "Jani" 100 (\x -> x - div x 4)
skver = Master "Skver" 100 (\x -> div (x+4) 2)
potionMaster =
  let plx x
        | x > 85  = x - plx (div x 2)
        | x == 60 = 31
        | x >= 51 = 1 + mod x 30
        | otherwise = x - 7
  in Master "PotionMaster" 170 plx

data Unit = M (State Mage) | E (State Entity) deriving (Eq)
instance Show Unit where
    show (M a) = show a
    show (E a) = show a

isAlive :: Unit -> Bool
isAlive (M (Alive _)) = True
isAlive (E (Alive _)) = True
isAlive _ = False
isDead :: Unit -> Bool
isDead = not . isAlive

formationFix :: Army -> Army
formationFix l = filter isAlive l ++ filter isDead l

over :: Army -> Bool
over = all isDead

updateHealth :: Unit -> (Integer -> Integer) -> Unit
updateHealth (M (Alive (Master n h sp))) s = M (if s h <= 0 then Dead else Alive (Master n (s h) sp))
updateHealth (E (Alive (Golem h))) s = E (if s h <= 0 then Dead else Alive (Golem (s h)))
updateHealth (E (Alive (HaskellElemental h))) s = E (if s h <= 0 then Dead else Alive (HaskellElemental (s h)))
updateHealth a _ =  a

fight :: EnemyArmy -> Army -> Army
fight [] l = l
fight _ [] = []
fight ((E (Alive (Golem a))):xs) (y:ys) = updateHealth y (+(-1)):fight xs ys
fight ((E (Alive (HaskellElemental a))):xs) (y:ys) = updateHealth y (+(-3)):fight xs ys
fight ((M (Alive (Master n h s))):xs) (y:ys) = updateHealth y s:fight xs [updateHealth a s | a <- ys]
fight (_:xs) (y:ys) = y:fight xs ys

haskellBlast :: Army -> Army
haskellBlast [] = []
haskellBlast l
    | length l <= 5 = [updateHealth a (+(-5))| a <- l]
    | otherwise = blast maxI where
        damage :: Unit -> Integer -> Int
        damage a d 
            | isAlive a = 1 +  damage (updateHealth a (+(-1))) (d-1) 
            | otherwise = 0
        damages = map haskellBlastHelp [0 .. length l - 5]
        maxD = maximum damages
        di = zip damages [0..]
        maxI = head [i | (d, i) <- di, d == maxD]
        haskellBlastHelp :: Int -> Int
        haskellBlastHelp i = sum [(damage x 5) | x <- take 5 (drop i l)]
        blast i = e ++ [updateHealth c (+(-5)) | c <- take 5 u] ++ drop 5 u  where
            (e, u) = splitAt i l

multiHeal :: Health -> Army -> Army
multiHeal h [] = []
multiHeal 0 l = l
multiHeal h l@(x:xs)
    | h < 0 = l
    | over l = l
    | h /= 0 = if nh /= 0 then multiHeal nh nl else nl where
        mh = multiHealHelp h l
        nl = fst mh
        nh = snd mh
        multiHealHelp 0 j = (j, 0)
        multiHealHelp h j@(a:as)
            | over j = (j, h)
            | otherwise = (updateHealth a (+1):fst mhh, snd mhh) where
                mhh = multiHealHelp (if isAlive a then h-1 else h) as
        multiHealHelp h [] = ([], h)

battle :: Army -> EnemyArmy -> Maybe Army
battle [] [] = Nothing
battle [] b = Just b
battle a [] = Just a
battle a b
    | over a && over b = Nothing
    | over a = Just b
    | over b = Just a
    | otherwise = battle fr en where
        fr = formationFix $ multiHeal 20 (haskellBlast $ fight b a)
        en = formationFix $ fight a b

chain :: Amount -> (Army, EnemyArmy) -> (Army, EnemyArmy)
chain _ ([], []) = ([], [])
chain s (a:as, []) = (updateHealth a (+s):as, [])
chain _ ([], b) = ([], b)
chain s (a:as, b:bs)
    | s <= 0 = (a:as, b:bs)
    | isDead a && isDead b = (a:fst(chain s (as, bs)), b:snd(chain s (as, bs)))
    | isDead a = (a:fst(chain (s-1) (as, bs)), updateHealth b (+(-s)):snd(chain (s-1) (as, bs)))
    | isDead b = (updateHealth a (+s):fst(chain (s-1) (as, bs)), b:snd(chain (s-1) (as, bs)))
    | s == 1 = (updateHealth a (+s):as, b:bs)
    | s == 2 = (updateHealth a (+s):as, updateHealth b (+(-(s-1))):bs)
    | otherwise = (updateHealth a (+s):fst ch, updateHealth b (+(-(s-1))):snd ch) where
        ch = chain (s-2) (as, bs)

battleWithChain :: Army -> EnemyArmy -> Maybe Army
battleWithChain [] [] = Nothing
battleWithChain [] b = Just b
battleWithChain a [] = Just a
battleWithChain a b
    | over a && over b {- || null a && null b -}= Nothing
    | over a {- || null a -} = Just b
    | over b {- || null b -}= Just a
    | otherwise = battleWithChain (formationFix (fst ch)) (formationFix (snd ch)) where
        fr = multiHeal 20 (haskellBlast (fight b a))
        en = fight a b
        ch = chain 5 (fr, en)

data OneVOne = Winner String | You Health OneVOne | HaskellMage Health OneVOne deriving Eq
instance Show OneVOne where
    show = showHelp True

showHelp top (You a b) = if top then "<You " ++ show a ++ "; " ++ showHelp False b else "You " ++ show a ++ "; " ++ showHelp False b
showHelp top (HaskellMage a b) = if top then "<HaskellMage " ++ show a ++ "; " ++ showHelp False b else "HaskellMage " ++ show a ++ "; " ++ showHelp False b
showHelp top (Winner a) = if top then "<|| Winner " ++ a ++ " ||>" else "|| Winner " ++ a ++ " ||>"

finalBattle :: Health -> Health -> OneVOne
finalBattle a b = finalBattleBuild (HaskellMage b (Winner ""), You a (Winner ""))

finalBattleAttack :: (OneVOne, OneVOne) -> (OneVOne, OneVOne)
finalBattleAttack (HaskellMage a _, You b _)
    | a <= 0 = (HaskellMage 0 (Winner ""), Winner "You")
    | otherwise = (You nb (Winner ""), HaskellMage na (Winner "")) where
        na
            | a < 4 = a*4
            | otherwise = a
        nb
            | a < 4 = b `div` 2
            | b > 20 = b*3 `div` 4
            | otherwise = b-11
finalBattleAttack (You a _, HaskellMage b _)
    | a <= 0 = (You 0 (Winner ""), Winner "HaskellMage")
    | otherwise = (HaskellMage nb (Winner ""), You na (Winner "")) where
        na
            | a < 4 = a*4
            | otherwise = a
        nb
            | a < 4 = b
            | b > 15 = b*3 `div` 5
            | otherwise = b-9

finalBattleBuild :: (OneVOne, OneVOne) -> OneVOne
finalBattleBuild (HaskellMage b d, Winner a) = Winner a
finalBattleBuild (You b d, Winner a) = Winner a
finalBattleBuild (HaskellMage a c, You b d) = HaskellMage (max a 0) (finalBattleBuild (finalBattleAttack (HaskellMage a c, You b d)))
finalBattleBuild (You a c, HaskellMage b d) = You (max a 0) (finalBattleBuild (finalBattleAttack (You a c, HaskellMage b d)))