class Warrior:
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")

# Создание экземпляра класса Warrior
war1 = Warrior("Степа", 25, 56, "коричневый")

# Вызов методов для вывода информации
print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)
war1.hit()
war1.walk()
war1.sleep()
war1.eat()
print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)

print(war2.name)
print(war2.power)
print(war2.endurance)
print(war2.hair_color)
war2.hit()
war2.walk()
war2.eat()
print(war2.name)
print(war2.power)
print(war2.endurance)
print(war2.hair_color)

