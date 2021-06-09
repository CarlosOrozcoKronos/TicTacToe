import juego
import os

os.system("cls" if os.name == "nt" else "clear")

juego = juego.Juego()
juego.turnoLooper()
