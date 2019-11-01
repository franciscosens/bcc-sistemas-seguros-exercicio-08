class Classe:
    def __init__(self):
        pass

    def cifrar(self, texto):
        pass

    def decifrar(self, cifra):
        pass

if __name__ == "__main__":
    conversor = Classe()
    cifrado = conversor.cifrar('')
    print(cifrado)
    texto = conversor.decifrar(cifrado)
    print(texto)

    