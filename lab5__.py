class Medicine:
    def __init__(self, name, price, quantity, needs_prescription, expiration_date):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.needs_prescription = needs_prescription
        self.expiration_date = expiration_date
        
    def is_expired(self, current_date):
        return self.expiration_date < current_date

    def apply_discount(self, percent=10):
        self.price = round(self.price * (1 - percent / 100), 2)

    def info(self):
        recipe = "за рецептом" if self.needs_prescription else "без рецепта"
        print(
            f"{self.name} | {self.price:.2f} грн | "
            f"кількість: {self.quantity} | {recipe} | до: {self.expiration_date}"
        )
class Pharmacy:
    def __init__(self):
        self.items = []

    def add(self, med):
        self.items.append(med)
    def remove(self, name):
       self.items = [
           m for m in self.items if m.name.lower() !=name.lower()
       ]
    def audit_expired(self, current_date):
        self.items = [
            m for m in self.items if not m.is_expired(current_date)
        ]

    def apply_discount_all(self, percent=10):
        for m in self.items:
            m.apply_discount(percent)

    def show_cheapest(self):
         if not self.items:
            print("У списку немає ліків.")
            return
        min_price = min(m.price for m in self.items)
        print("Найдешевші ліки:")
        for m in self.items:
           if m.price == min_price:
               m.info()

p = Pharmacy()
p.add(Medicine("Аспірин", 50.0, 15, False, "2027-05-01"))
p.add(Medicine("Парацетамол", 30.0, 20, False, "2026-10-01"))
p.show()
p.audit_expired("2026-11-25")
p.apply_discount_all(10)
p.show_cheapest()
p.show()
