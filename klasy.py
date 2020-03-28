class Projekt:
    def __init__(self):
        self.name="imie"
        self.id=123
        self.price=12.5

    def dispaly(self):
        print(self.name)
        print(self.id)
        print(self.price)

p1=Projekt()
p1.dispaly()