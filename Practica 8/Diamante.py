class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1
obj_a = A(10, 20)
obj_b = B(30, 40)
obj_d = D(50, 60, 70)

print("Clase A")
print(f"Antes: x={obj_a.x}, z={obj_a.z}")
obj_a.incrementaXZ()
print(f"Después de incrementaXZ(): x={obj_a.x}, z={obj_a.z}")

print("\nClase B")
print(f"Antes: y={obj_b.y}, z={obj_b.z}")
obj_b.incrementaYZ()
print(f"Después de incrementaYZ(): y={obj_b.y}, z={obj_b.z}")

print("\nClase D")
print(f"Antes: x={obj_d.x}, y={obj_d.y}, z={obj_d.z}")
obj_d.incrementaXYZ()
print(f"Después de incrementaXYZ(): x={obj_d.x}, y={obj_d.y}, z={obj_d.z}")