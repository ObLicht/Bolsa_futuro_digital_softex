class Musica:
    def __init__(self, titulo, cantor):
        self.titulo = titulo
        self.cantor = cantor

class Playlist:
    def __init__(self):
        self.playlist = []

    def adicionarMusica(self, musica: Musica):
        self.playlist.append(musica)
    
    def mostrarPlaylist(self):
        for musica in self.playlist:
            print(f"Título: {musica.titulo}, Cantor: {musica.cantor}")

musica1 = Musica("Always and Forever", "José")
musica2 = Musica("I Will Go", "André")

playlist1 = Playlist()
playlist1.adicionarMusica(musica1)
playlist1.adicionarMusica(musica2)

playlist1.mostrarPlaylist()
