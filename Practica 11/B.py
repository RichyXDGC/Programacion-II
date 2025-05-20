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
    
    def incrementar_precio(self, incremento):
        self.precio += incremento

# a. Crear dos objetos pintura que tengan anuncios de venta

artista_x = Artista("Leonardo", "11111", 12)
artista_y = Artista("Miguel", "22222", 8)
artista_z = Artista("Rafael", "33333", 15)

pintura1 = Pintura("Paisaje montañoso", "Óleo", "Paisaje")
pintura1.agregar_artista(artista_x)
pintura1.agregar_artista(artista_y)
anuncio1 = Anuncio("A001", 7500)
pintura1.anuncio = anuncio1

pintura2 = Pintura("Retrato familiar", "Acrílico", "Retrato")
pintura2.agregar_artista(artista_z)
anuncio2 = Anuncio("A002", 9200)
pintura2.anuncio = anuncio2

# b. Calcular el promedio de años Experiencia de los artistas de ambas pinturas
def promedio_experiencia(pinturas):
    total_artistas = 0
    suma_experiencia = 0
    
    for pintura in pinturas:
        for artista in pintura.artistas:
            total_artistas += 1
            suma_experiencia += artista.añosExperiencia
    
    return suma_experiencia / total_artistas if total_artistas > 0 else 0

pinturas = [pintura1, pintura2]
print(f"Promedio de años de experiencia: {promedio_experiencia(pinturas):.1f} años")

# c. Incrementar el precio en X a la pintura del artista con nombre X
def incrementar_precio_artista(pinturas, nombre_artista, incremento):
    for pintura in pinturas:
        for artista in pintura.artistas:
            if artista.nombre == nombre_artista and hasattr(pintura, 'anuncio'):
                pintura.anuncio.incrementar_precio(incremento)
                print(f"Precio actualizado para obra de {nombre_artista}. Nuevo precio: ${pintura.anuncio.precio}")
                return
    print(f"No se encontró artista con nombre {nombre_artista} o la obra no tiene anuncio")

incrementar_precio_artista(pinturas, "Leonardo", 1000)
incrementar_precio_artista(pinturas, "Rafael", 1500)