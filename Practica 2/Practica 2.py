import math
import turtle

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x * self.x + self.y * self.y)
        angulo = math.atan2(self.y, self.x)  
        angulo = math.degrees(angulo)
        return radio, angulo

    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x, self.y)

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def toString(self):
        return "Línea de {} a {}".format(self.p1, self.p2)

    def dibujalinea(self):
        turtle.penup()
        turtle.goto(self.p1.x, self.p1.y)
        turtle.pendown()
        turtle.goto(self.p2.x, self.p2.y)
        turtle.penup()

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def toString(self):
        return "Círculo con centro en {} y radio {:.2f}".format(self.centro, self.radio)

    def dibujacirculo(self):
        turtle.penup()
        turtle.goto(self.centro.x, self.centro.y - self.radio)
        turtle.pendown()
        turtle.circle(self.radio)
        turtle.penup()

turtle.speed(1) 
turtle.pensize(2)  

p1 = Punto(0, 100)
p2 = Punto(100, 0)

linea = Linea(p1, p2)
print(linea.toString())
linea.dibujalinea()

circulo = Circulo(p1, 50)
print(circulo.toString())
circulo.dibujacirculo()

turtle.done()
