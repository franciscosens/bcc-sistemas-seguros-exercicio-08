from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

class Classe:
    def __init__(self):
        self.texto_cifrado = b'.N,v\xc6B2\x1d\xba\xd4\xb1\xa37\xed\xb1\x83\xae\xa6h,\x0b\xbf=\x13NP>d\x1d\xac\xea\x19f\x83\r\xa9+\xf9\x9c\x12[\xbf\xeb\n(qQ\xe2J\xda\xcc\xb5\xa4\x9d\xddoS\x86\xf1\xe8\x0e\x9e\xefY'
        self.chave_cifrada = b'\x05e)b\xc5\xe7\xe6\xba\x81\xff\x9e\xa2K\xb1\x9d\xb1\x1e\xa9\xc3cQm:\x86\x07\x1c\xe3\xeb\xa0\x05q\xd3\xafH\x86#\x08\xdd\xe2\x01/\x10+\x1f\xa6-/ob\xf7\xf5\x1c^\xcf\xc9Z-\xe0\x1d\x19\xbfpH\xd2}\xf7\xb9\x05\xd1\xe9\xf0\xf43+\xee\xca\tVZ\x86\x94{P\xd8B\xfc\xfb\xe7h&\xad\x82L7O*\x084\xf6R\x952!\x9a\xf5J\x16\xe4\xb0\x9f\xee\r\xc5vn_\xfe\xefy\x15@X\xbf"\xfc=\xa8:'
        self.chave_privada = self.ler_arquivo('chave_privada.txt')
        self.chave = self.decifrar_chave()
        self.texto_decrifado = self.decifrar_texto()
        print("Texto:", self.texto_decrifado )
        

    def decifrar_chave(self):
        key = RSA.import_key(self.chave_privada)
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(self.chave_cifrada)

    def ler_arquivo(self, nome):
        f = open(nome, mode="r", encoding="utf-8")
        texto = f.read()
        return texto

    def decifrar_texto(self):
        cipher = AES.new(self.chave, AES.MODE_ECB)
        texto_decifrado = cipher.decrypt(self.texto_cifrado)
        return unpad(texto_decifrado, 32).decode("utf-8")

if __name__ == "__main__":
    conversor = Classe()