class Configuracion:
    _instancia = None  # Variable de clase que almacenará la única instancia

    def __new__(cls):
        # __new__ se llama antes que __init__ y es responsable de crear la instancia
        if cls._instancia is None:
            # Si aún no hay instancia, se crea una nueva y se guarda
            cls._instancia = super().__new__(cls)
            cls._instancia.valor = "Valor por defecto"  # Se le asigna un valor inicial
        return cls._instancia  # Siempre devuelve la misma instancia

    def get_valor(self):
        return self.valor  # Devuelve el valor actual

    def set_valor(self, valor):
        self.valor = valor  # Cambia el valor almacenado en la instancia


# --------- Prueba del Singleton ---------
if __name__ == "__main__":
    config1 = Configuracion()
    print("Valor inicial:", config1.get_valor())

    # Cambiamos el valor desde config1
    config1.set_valor("Nuevo valor global")

    # Creamos otra referencia, pero apunta al mismo objeto
    config2 = Configuracion()
    print("Valor desde config2:", config2.get_valor())

    # Verificamos que ambas referencias son la misma instancia
    if config1 is config2:
        print("Ambas instancias son la misma (Singleton funciona)")
