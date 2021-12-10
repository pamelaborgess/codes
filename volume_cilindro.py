def area(raio):
    import math
    calc = math.pi*raio*raio
    return calc

def volume(area,lado):
    print(area*lado)

raio = int(input("Raio: "))
lado = int(input("Lado: "))

volume(area(raio),lado)