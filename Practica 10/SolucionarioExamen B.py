class Ministerio:
    def __init__(self, nombre, direccion, nroEmpleados, empleados=None, edades=None, sueldos=None):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = nroEmpleados
        self.empleados = empleados if empleados else [['' for _ in range(100)] for _ in range(3)]
        self.edades = edades if edades else [0] * 100
        self.sueldos = sueldos if sueldos else [0.0] * 100

    def mostrar_empleados(self):
        print(f"\nEmpleados del Ministerio: {self.nombre}")
        for i in range(self.nroEmpleados):
            print(f"{self.empleados[0][i]} {self.empleados[1][i]} {self.empleados[2][i]} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")

    # d) Polimorfismo por comportamiento: mostrar menor edad o menor sueldo
    def mostrar_empleado_menor(self, criterio='edad'):
        if criterio == 'edad':
            menor = min(self.edades[:self.nroEmpleados])
            print("\nEmpleado(s) con menor edad:")
            for i in range(self.nroEmpleados):
                if self.edades[i] == menor:
                    print(f"{self.empleados[0][i]} {self.empleados[1][i]} {self.empleados[2][i]} - Edad: {menor}")
        elif criterio == 'sueldo':
            menor = min(self.sueldos[:self.nroEmpleados])
            print("\nEmpleado(s) con menor sueldo:")
            for i in range(self.nroEmpleados):
                if self.sueldos[i] == menor:
                    print(f"{self.empleados[0][i]} {self.empleados[1][i]} {self.empleados[2][i]} - Sueldo: {menor}")
        else:
            print("Criterio inválido.")

    # b) Eliminar empleados con edad X
    def eliminar_empleado_por_edad(self, edad_objetivo):
        i = 0
        while i < self.nroEmpleados:
            if self.edades[i] == edad_objetivo:
                print(f"Eliminando a: {self.empleados[0][i]} {self.empleados[1][i]} {self.empleados[2][i]}")
                for j in range(i, self.nroEmpleados - 1):
                    for k in range(3):
                        self.empleados[k][j] = self.empleados[k][j + 1]
                    self.edades[j] = self.edades[j + 1]
                    self.sueldos[j] = self.sueldos[j + 1]
                self.nroEmpleados -= 1
            else:
                i += 1

    # c) Sobrecarga del operador '+' para transferir un empleado del segundo al primero
    def __add__(self, other):
        if other.nroEmpleados == 0:
            print("No hay empleados para transferir.")
            return self

        if self.nroEmpleados >= 100:
            print("No hay espacio en este ministerio.")
            return self

        # Transferencia del último empleado
        pos_from = other.nroEmpleados - 1
        pos_to = self.nroEmpleados

        for i in range(3):
            self.empleados[i][pos_to] = other.empleados[i][pos_from]
        self.edades[pos_to] = other.edades[pos_from]
        self.sueldos[pos_to] = other.sueldos[pos_from]

        other.nroEmpleados -= 1
        self.nroEmpleados += 1

        print(f"Empleado transferido de {other.nombre} a {self.nombre}")
        return self


# a) Instanciar 2 objetos Ministerio de diferente forma
empleados_datos = [
    ["Pedro", "Lucy", "Ana", "Saul"],  
    ["Rojas", "Sosa", "Perez", "Arce"],  
    ["Luna", "Rios", "Rojas", "Calle"]   
]
edades = [35, 43, 26, 29]
sueldos = [2500, 3250, 2700, 2500]

ministerio1 = Ministerio("Ministerio de Educación", "Calle Ayacucho N°123", 4, empleados_datos, edades, sueldos)

# Segunda forma: objeto vacío
ministerio2 = Ministerio("Ministerio de Salud", "Av. Saavedra Esq. 10", 0)

# Mostrar datos iniciales
ministerio1.mostrar_empleados()
ministerio2.mostrar_empleados()

# b) Eliminar empleados con edad X
print("\n--- Eliminando empleados con edad 43 ---")
ministerio1.eliminar_empleado_por_edad(43)
ministerio1.mostrar_empleados()

# c) Transferir un empleado del segundo ministerio al primero
print("\n--- Agregando un nuevo empleado a ministerio2 ---")
ministerio2.empleados[0][0] = "Carlos"
ministerio2.empleados[1][0] = "Zeballos"
ministerio2.empleados[2][0] = "Quispe"
ministerio2.edades[0] = 31
ministerio2.sueldos[0] = 2800
ministerio2.nroEmpleados = 1

print("\n--- Transfiriendo un empleado de ministerio2 a ministerio1 ---")
ministerio1 + ministerio2
ministerio1.mostrar_empleados()
ministerio2.mostrar_empleados()

# d) Mostrar menor edad y menor sueldo
print("\n--- Mostrar empleados con menor edad (ministerio1) ---")
ministerio1.mostrar_empleado_menor("edad")

print("\n--- Mostrar empleados con menor sueldo (ministerio1) ---")
ministerio1.mostrar_empleado_menor("sueldo")
