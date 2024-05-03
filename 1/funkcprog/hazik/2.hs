type CurrentDistrict = Int
type NextDistrict = Int
type HealthDamage = Int
type ArmorDamage = Int
type Health = Int
type Armor = Int
type Enhance = Int

move :: (CurrentDistrict , NextDistrict) -> NextDistrict
move (a, b) = b

arcane_missiles :: (HealthDamage , ArmorDamage) -> (Health , Armor) -> (Health , Armor)
arcane_missiles (a, b) (c, d) = (c-a, d-b) 

arcane_missiles_mark_1 :: Enhance -> (HealthDamage , ArmorDamage) -> (Health , Armor) -> (Health , Armor)
arcane_missiles_mark_1 e (a, b) (c, d) = (c-a*e, d-b*e) 

arcane_blast :: (HealthDamage , ArmorDamage) -> (HealthDamage , ArmorDamage) -> (Health , Armor) -> (Health , Armor)
arcane_blast (a, b) (c, d) (e, f) = (e-(a * c + b * d), f-(a * c + b * d))
