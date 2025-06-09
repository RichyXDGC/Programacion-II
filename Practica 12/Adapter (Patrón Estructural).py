# Clase base que define la interfaz esperada
class ReproductorAudio:
    def reproducir(self, formato, archivo):
        pass  # Esta función debe ser implementada por las clases hijas


# Clase que tiene una interfaz diferente (no compatible directamente)
class ReproductorAvanzado:
    def reproducir_mp4(self, archivo):
        print(f"Reproduciendo MP4: {archivo}")

    def reproducir_vlc(self, archivo):
        print(f"Reproduciendo VLC: {archivo}")


# Adaptador que traduce la interfaz antigua a la nueva
class AdaptadorReproductor(ReproductorAudio):
    def __init__(self):
        self.reproductor = ReproductorAvanzado()  # Instancia del nuevo reproductor

    def reproducir(self, formato, archivo):
        # Adaptamos el formato a los métodos del nuevo reproductor
        if formato == "mp4":
            self.reproductor.reproducir_mp4(archivo)
        elif formato == "vlc":
            self.reproductor.reproducir_vlc(archivo)
        else:
            print(f"Formato no soportado: {formato}")


# --------- Prueba del Adaptador ---------
if __name__ == "__main__":
    reproductor = AdaptadorReproductor()
    reproductor.reproducir("mp4", "video1.mp4")  # Usa método adaptado
    reproductor.reproducir("vlc", "video2.vlc")  # Usa otro método adaptado
    reproductor.reproducir("avi", "video3.avi")  # Formato no soportado
