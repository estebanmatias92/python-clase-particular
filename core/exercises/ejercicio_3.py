import random
import os


class Ahorcado:
    def __init__(self):
        self.palabras = ["c++", "python", "csharp", "unity"]
        self.inic()

    def inic(self):
        self.valin()

        while not self.condit1() and not self.condit2():
            os.system("clear")
            print("A H O R C A D O")
            ## print(self.palabra) Muestra la palabra
            print("Intentos", self.intentos)
            print("Letras adivinadas: ", self.letras_adivinadas)
            self.letra = input("Ingrese letra: ").lower()
            self.letra = self.letra

            self.probar_letra()
            print(self.letra)
        os.system("clear")
        print("Termino el juego")

        if self.intentos <= 0:
            print("Perdiste!")
            print("La palabra era: {}".format(self.palabra))
        else:
            print("Ganaste")
            print("La palabra era: {}".format(self.palabra))
            print("Vidas restantes: {}".format(self.intentos))

    def valin(self):
        self.palabra = random.choice(self.palabras)
        self.intentos = 7
        self.letras_faltantes = set(self.palabra)
        self.letras_adivinadas = set()

    def probar_letra(self):
        if self.letra in self.letras_faltantes:
            self.letras_adivinadas.add(self.letra)
            self.letras_faltantes.remove(self.letra)
        else:
            self.intentos -= 1

    def condit1(self):
        if self.intentos == 0:
            return True
        else:
            return False

    def condit2(self):
        return not self.letras_faltantes


JuegoAhorcado = Ahorcado()
I = True
while I == True:
    continuar = input("Continuar? Y/N ")
    if continuar == "Y":
        Ahorcado()
    else:
        break
