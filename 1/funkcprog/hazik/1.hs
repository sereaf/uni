inc :: Int -> Int
inc a = a + 1

lesser_heal :: Int -> Int
lesser_heal a = inc(inc(inc a))

lookout :: Int -> Int -> Bool
lookout a b = a > (div b 10)

volume :: Int -> Int -> Int
volume a b = a + (b * (mod a 12))