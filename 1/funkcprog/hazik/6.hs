type Crate item = [[item]]
type Recipe item = (item -> Bool)
type Measure item = (item -> item)
type Amount = Int

recipe :: Eq item => Recipe item -> Crate item -> Bool
{- recipe :: Eq item => (item -> Bool) ->[[item]] -> Bool -}
-- recipe (>3) [[4,4],[5,4]]
recipe a = all (all a)

measure :: Measure item -> Crate item -> Crate item
measure f a = [[f y | y <- x] | x <- a]

measure_until :: Eq item => Recipe item -> Measure item -> Crate item {-not empty-} -> Amount
measure_until a b c
    | all (all a) c = 1 + measure_until a b [[b y | y <- x] | x <- c]
    | otherwise = 0