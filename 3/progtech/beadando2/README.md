# Kitolás
Készítsünk programot, amellyel a következő két személyes játékot lehet játszani. Adott egy
n × n mezőből álló tábla, amelyen kezdetben a játékosoknak n fehér, illetve n fekete kavics áll
rendelkezésre, amelyek elhelyezkedése véletlenszerű. A játékos kiválaszthat egy saját
kavicsot, amelyet függőlegesen, vagy vízszintesen eltolhat. Eltoláskor azonban nem csak az
adott kavics, hanem a vele az eltolás irányában szomszédos kavicsok is eltolódnak, a szélső
mezőn lévők pedig lekerülnek a játéktábláról. A játék célja, hogy adott körszámon belül (5n)
az ellenfél minél több kavicsát letoljuk a pályáról (azaz nekünk maradjon több kavicsunk). Ha
mindkét játékosnak ugyanannyi marad, akkor a játék döntetlen.
A program biztosítson lehetőséget új játék kezdésére a táblaméret (3×3, 4×4, 6×6) és így a
lépésszám (15, 20, 30) megadásával, és ismerje fel, ha vége a játéknak. Ekkor jelenítse meg,
hogy melyik játékos győzött (ha nem lett döntetlen), majd kezdjen automatikusan új játékot.