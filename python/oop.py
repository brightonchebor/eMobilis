class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def drive(self):
        print(f'The {self.color} {self.model} is driving')
benz = Car('benz', 'red')
print(benz.color)
print(benz.model)
print(benz.drive())