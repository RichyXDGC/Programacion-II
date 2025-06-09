# Clase base de los observadores (no es obligatorio en Python, pero ayuda a entender la estructura)
class Observador:
    def actualizar(self, temperatura):
        pass  # Método que debe implementarse en cada observador concreto


# Sujeto observado: genera eventos que otros quieren escuchar
class EstacionMeteorologica:
    def __init__(self):
        self._observadores = []  # Lista de observadores suscritos
        self._temperatura = 0.0  # Temperatura inicial

    def agregar_observador(self, obs):
        self._observadores.append(obs)  # Agrega un observador a la lista

    def eliminar_observador(self, obs):
        self._observadores.remove(obs)  # Elimina un observador

    def notificar_observadores(self):
        # Llama a todos los observadores cuando hay una actualización
        for obs in self._observadores:
            obs.actualizar(self._temperatura)

    def set_temperatura(self, temperatura):
        # Actualiza la temperatura y notifica a todos los observadores
        self._temperatura = temperatura
        print(f"\nNueva temperatura: {temperatura}°C")
        self.notificar_observadores()


# Observador que muestra la temperatura
class PantallaTemperatura(Observador):
    def actualizar(self, temperatura):
        print(f"PantallaTemperatura -> Temperatura actual: {temperatura}°C")


# Observador que muestra una estimación de humedad
class PantallaHumedad(Observador):
    def actualizar(self, temperatura):
        humedad = 100 - temperatura  # Fórmula simulada para ejemplo
        print(f"PantallaHumedad -> Humedad estimada: {humedad:.1f}%")


# --------- Prueba del patrón Observer ---------
if __name__ == "__main__":
    estacion = EstacionMeteorologica()

    pantalla1 = PantallaTemperatura()
    pantalla2 = PantallaHumedad()

    estacion.agregar_observador(pantalla1)
    estacion.agregar_observador(pantalla2)

    estacion.set_temperatura(30.5)  # Notifica a ambos observadores
    estacion.set_temperatura(25.0)  # Nueva notificación
