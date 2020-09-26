class Animals:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight

    def feed(self, value):
        self.weight += value
        return "покормили"


class Egg_laying(Animals):  # несущие яйца
    # Какой из 2х вариантов правильнее?
    # 1
    def do_lay(self):
        return "несет яйца"

    def do_smth(self):
        return "которое " + Egg_laying.do_lay(self)

    # 2
    # def do_smth(self):
    #     return 'которое несет яйца'


class Chicken(Egg_laying):
    representative = "Курица"

    def do_voice(self):
        return "Кококо"


class Goose(Egg_laying):
    representative = "Гусь"

    def do_voice(self):
        return "Га-га"


class Duck(Egg_laying):
    representative = "Утка"

    def do_voice(self):
        return "Кря-кря"


class Shearing(Animals):  # Стригущиеся
    def do_smth(self):
        return "которое cтрижется"


class Sheep(Shearing):
    representative = "Овца"

    def do_voice(self):
        return "Бееее"


class Milking(Animals):  # доящиеся
    def do_smth(self):
        return "которое доится"


class Cow(Milking):
    representative = "Корова"

    def do_voice(self):
        return "Муууу"


class Goat(Milking):
    representative = "Коза"

    def do_voice(self):
        return "Мееее"


feed_value = 2
farm = [
    Chicken("Ко-ко", 6),
    Chicken("Кукареку", 7),
    Goose("Белый", 12),
    Goose("Серый", 14),
    Duck("Кряква", 8),
    Sheep("Барашек", 80),
    Sheep("Кудрявый", 90),
    Cow("Манька", 150),
    Goat("Дереза", 60),
    Goat("Копытце", 70),
]

max_weight = sum_weight = 0
for animal in farm:
    print(
        f'{animal.representative} "{animal.name}" - это животное, {animal.do_smth()} и говорит {animal.do_voice()}, вес = {animal.weight}, и мы его {animal.feed(feed_value)} на {feed_value}'
    )
    sum_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        represent = animal.representative
print(f"Вес всех животных = {sum_weight}")
print(f"Самое тяжелое животное - это {represent} с весом = {max_weight}")
