class Medicine:
    def init(self, name, price):
        self.name = name
        self.price = price

class Pharmacy:
    def init(self):
        self.items = []

    def add(self, med):
        self.items.append(med)

    def show(self):
        for m in self.items:
            print(m.name, "-", m.price, "грн")

p = Pharmacy()
p.add(Medicine("Аспірин", 50))
p.add(Medicine("Парацетамол", 30))
p.show()