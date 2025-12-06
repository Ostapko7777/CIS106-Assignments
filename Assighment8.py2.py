# Part 2 - Car and Sport Classes

class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90


class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"

    def set_sport_wheels(self, option):
        self.sport_wheels = option

    def set_sport_engine(self, option):
        self.sport_engine = option

    def set_sport_interior(self, option):
        self.sport_interior = option

    def price_with_options(self):
        price = self.discount_price()

        if self.sport_wheels == "Y":
            price += 1000
        if self.sport_engine == "Y":
            price += 3000
        if self.sport_interior == "Y":
            price += 2000

        return price


# ----- Test the classes -----
car = Sport("Toyota", "Supra", 50000)
car.set_sport_wheels("Y")
car.set_sport_engine("Y")
car.set_sport_interior("N")

print("Car:", car.make, car.model)
print("Base Discount Price:", car.discount_price())
print("Final Price with Options:", car.price_with_options())
