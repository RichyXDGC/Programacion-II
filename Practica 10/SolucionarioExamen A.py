class LineaTeleferico:
    def __init__(self, color, tramo, nroCabinas, nroEmpleados, empleados=None, edades=None, sueldos=None):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = nroEmpleados
        self.empleados = empleados if empleados else [['', '', ''] for _ in range(100)]
        self.edades = edades if edades else [0] * 100
        self.sueldos = sueldos if sueldos else [0.0] * 100

    def mostrar_empleados(self):
        print(f"Empleados de línea {self.color}:")
        for i in range(self.nroEmpleados):
            nombre, ap1, ap2 = self.empleados[i]
            print(f"{nombre} {ap1} {ap2} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")

    # d) Método sobrecargado: polimorfismo por comportamiento
    def mostrar_empleado_mayor(self, criterio='edad'):
        if criterio == 'edad':
            mayor = max(self.edades[:self.nroEmpleados])
            print("\nEmpleado(s) con mayor edad:")
            for i in range(self.nroEmpleados):
                if self.edades[i] == mayor:
                    print(f"{self.empleados[i]} - Edad: {mayor}")
        elif criterio == 'sueldo':
            mayor = max(self.sueldos[:self.nroEmpleados])
            print("\nEmpleado(s) con mayor sueldo:")
            for i in range(self.nroEmpleados):
                if self.sueldos[i] == mayor:
                    print(f"{self.empleados[i]} - Sueldo: {mayor}")
        else:
            print("Criterio inválido.")

    # b) Eliminar empleados con apellido X
    def eliminar_empleado_por_apellido(self, apellido):
        i = 0
        while i < self.nroEmpleados:
            if apellido in self.empleados[i]:
                print(f"Eliminando a: {self.empleados[i]}")
                # mover todo hacia arriba
                for j in range(i, self.nroEmpleados - 1):
                    self.empleados[j] = self.empleados[j + 1]
                    self.edades[j] = self.edades[j + 1]
                    self.sueldos[j] = self.sueldos[j + 1]
                self.nroEmpleados -= 1
            else:
                i += 1

    # c) Sobrecargar el operador '+' para transferir un empleado a otra línea
    def __add__(self, other):
        # Transferir el último empleado de self a other
        if self.nroEmpleados == 0:
            print("No hay empleados para transferir.")
            return self

        if other.nroEmpleados >= 100:
            print("No hay espacio en la otra línea.")
            return self

        # Transferencia
        empleado = self.empleados[self.nroEmpleados - 1]
        edad = self.edades[self.nroEmpleados - 1]
        sueldo = self.sueldos[self.nroEmpleados - 1]

        other.empleados[other.nroEmpleados] = empleado
        other.edades[other.nroEmpleados] = edad
        other.sueldos[other.nroEmpleados] = sueldo
        other.nroEmpleados += 1

        self.nroEmpleados -= 1

        print(f"Empleado {empleado} transferido de {self.color} a {other.color}")
        return self
    
# a) Instanciar 2 objetos

# Primera forma
linea1 = LineaTeleferico("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio", 20, 4,
    empleados=[
        ["Pedro", "Rojas", "Luna"],
        ["Lucy", "Sosa", "Rios"],
        ["Ana", "Perez", "Rojas"],
        ["Saul", "Arce", "Calle"]
    ],
    edades=[35, 43, 26, 29],
    sueldos=[2500, 3250, 2700, 2500]
)

# Segunda forma: crear vacío y llenar manualmente
linea2 = LineaTeleferico("Verde", "Estación A, Estación B", 15, 0)
# b) Eliminar a los empleados con apellido "Rojas"

linea1.eliminar_empleado_por_apellido("Rojas")

# c) Transferir un empleado de linea1 a linea2

linea1 + linea2

# d) Mostrar empleados con mayor edad o sueldo

linea1.mostrar_empleado_mayor("edad")
linea2.mostrar_empleado_mayor("sueldo")
