def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 5))


def calculate(**kwargs):
    print(kwargs)


class Car:

    def __init__(self, **kw):
        self.model = kw['model']
        self.color = kw['color']
        self.year = kw['year']
        self.mileage = kw['mileage']


mycar = Car(model='Tesla', color='black', year=2020, mileage=0)

print(mycar.model)
