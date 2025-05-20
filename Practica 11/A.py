class Artista:
    def __init__(self, nombre, ci, añosExperiencia):
        self.nombre = nombre
        self.ci = ci
        self.añosExperiencia = añosExperiencia

class Obra:
    def __init__(self, titulo, material):
        self.titulo = titulo
        self.material = material
        self.artistas = []
    
    def agregar_artista(self, artista):
        self.artistas.append(artista)

class Pintura(Obra):
    def __init__(self, titulo, material, genero):
        super().__init__(titulo, material)
        self.genero = genero

class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

# a. Crear un objeto pintura que tenga un anuncio y otro objeto pintura sin anuncio

artista1 = Artista("MIGUEL", "12345", 10)
artista2 = Artista("RAFAEL", "67890", 15)

pintura_con_anuncio = Pintura("Obra con anuncio", "Óleo", "Retrato")
pintura_con_anuncio.agregar_artista(artista1)
pintura_con_anuncio.agregar_artista(artista2)
anuncio1 = Anuncio("001", 5000)
pintura_con_anuncio.anuncio = anuncio1  

pintura_sin_anuncio = Pintura("Obra sin anuncio", "Acuarela", "Paisaje")
pintura_sin_anuncio.agregar_artista(Artista("a3", "54321", 8))

# b. Mostrar el nombre del artista con más años de Experiencia de ambas pinturas
def artista_mas_experiencia(pinturas):
    max_experiencia = 0
    artista_experto = None
    
    for pintura in pinturas:
        for artista in pintura.artistas:
            if artista.añosExperiencia > max_experiencia:
                max_experiencia = artista.añosExperiencia
                artista_experto = artista.nombre
    
    return artista_experto

pinturas = [pintura_con_anuncio, pintura_sin_anuncio]
print(f"El artista con más experiencia es: {artista_mas_experiencia(pinturas)}")

# c. Agregar un anuncio de venta a la pintura sin anuncio y calcular el monto total de venta
anuncio2 = Anuncio("002", 3000)
pintura_sin_anuncio.anuncio = anuncio2

def monto_total_venta(pinturas):
    total = 0
    for pintura in pinturas:
        if hasattr(pintura, 'anuncio') and pintura.anuncio is not None:
            total += pintura.anuncio.precio
    return total

print(f"El monto total de venta es: ${monto_total_venta(pinturas)}")