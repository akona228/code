class Pet:
    def init(self, name, kind):
        self.name = name
        self.kind = kind  
        self.energy = 5

    def eat(self):
        self.energy += 2
        print(f"{self.name} наелся и спит")

    def sleep(self):
        self.energy = 10
        print(f"{self.name} крепко спит... Zzz")

    def play(self):
        if self.energy > 2:
            self.energy -= 2
            sound = "мяу!" if self.kind == "cat" else "гав!"
            print(f"{self.name} бормочит и мурлычит: {sound}")
        else:
            print(f"{self.name} устав")

cat = Pet("Рафик", "cat")
dog = Pet("Обама", "dog")

cat.play()
cat.eat()
cat.sleep()

dog.play()
dog.play()
dog.sleep()