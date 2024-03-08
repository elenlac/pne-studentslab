class Seq:
    def __init__(self, strbases):

    # STRBASES = cuando contruyamos un objeto de nuestra clase tenemos que pasarle un string, esto es un ATRIBUTO
        self.strbases = strbases

class Point2D:

    # de manera predeterminada los valores de x e y es 0:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x=0, y=0):  # esta versión es la más válida
        self.x = x
        self.y = y


# PRIMERA FORMA DE HACERLO
class Person:
    def __init__(self, name:str, age:int):  # toda persona tiene dos atributos
        self.name = name  # si inviertes el orden del = no tiene sentido porque no has definido primero el atributo
        self.age = age  # almacena el valor del parámetro age que nos pasan
        self.scores = []

    def show(self):
        print(f"Name: {self.name} \nAge: {self.age} \nScores: {self.scores}")

p1 = Person("Elena", 18)
p1.show()  # si lo pones con un print me imprime lo que devuelve show que es None



# SEGUNDA FORMA DE HACERLO (CON STR)

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.scores = []

    def __str__(self):  # sino está y hacemos print(objeto) nos devuelve: <__main__.Person object at 0x000001F67AFA4A10>
        return f"Name: {self.name} \nAge: {self.age} \nScores {self.scores}"

    def is_older(self):
        """if self.age >= 18:
            return True
        else:
            return False"""
        return self.age >= 18

    def add_score(self, score):
        self.scores.append(score)


print("\n")

p2 = Person("Inés", 19)
print(p2)

print("\n")

print(f"Is older? {p2.is_older()}")
p2.add_score(7.5)
print(p2)
