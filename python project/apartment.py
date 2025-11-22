from os import name


class Apartment:
    def init(self, price, area, floor, balcony, rooms, district):
        self.price = float(price)
        self.area = float(area)
        self.floor = int(floor)
        self.balcony = bool(balcony)
        self.rooms = int(rooms)
        self.district = district.strip()
        self.sold = False
        self.owner = None

    def buy(self, name):
        if self.sold:
            print("Лошок, уже продано")
            return
        self.owner = name.strip()
        self.sold = True
        print("Попытай удачу еще раз")

    def sell(self):
        if not self.sold:
            print("Чего смотришь, или бери или уходи")
            return
        self.owner = None
        self.sold = False
        print("Продаем, опятб")

    def renovate(self, price=None, area=None):
        if price is not None:
            self.price = float(price)
        if area is not None:
            self.area = float(area)
        print("На лево сходили")

    def info(self):
        return (f"Цена: {self.price}, Площадь: {self.area} м², Этаж: {self.floor}, "
                f"Балкон: {'да' if self.balcony else 'нет'}, Комнат: {self.rooms}, "
                f"Район: {self.district}, Статус: {'продана' if self.sold else 'в продаже'}")


def opt(prompt, cast):
    s = input(prompt).strip()
    return cast(s) if s != "" else None

def yn(prompt):
    return input(prompt).strip().lower().startswith("y")

def main():
    price = input("Цена: ")
    area = input("Площадь: ")
    floor = input("Этаж: ")
    balcony = yn("Балкон (y/n): ")
    rooms = input("Комнат: ")
    district = input("Район: ")
    a = Apartment(price, area, floor, balcony, rooms, district)

    while True:
        print("1) info  2) buy  3) sell  4) renovate  5) exit")
        c = input("> ").strip()
        if c == "1":
            print(a.info())
        elif c == "2":
            a.buy(input("Имя покупателя: "))
        elif c == "3":
            a.sell()
        elif c == "4":
            np = opt("Новая цена (Enter пропустить): ", float)
            na = opt("Новая площадь (Enter пропустить): ", float)
            a.renovate(price=np, area=na)
        elif c == "5":
            break

if name == "main":
    main()