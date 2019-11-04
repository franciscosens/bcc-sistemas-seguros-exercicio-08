from Crypto.Util.Padding import pad, unpad
import tkinter as tk
import binascii
import os
from tkinter import filedialog
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

class Questao02:
    def __init__(self,):
        self.solicitar_arquivo()
        self.texto_arquivo = self.ler_arquivo()
        self.texto_arquivo_byte = bytearray(self.texto_arquivo.encode("utf-8"))

        self.chave = 'abcdefghijklmnop'
        self.chave_byte = bytearray(self.chave.encode("utf-8"))
        self.chave_publica = self.obter_chave_publica()

        self.chave_cifrada = self.cifrar_chave()
        self.texto_cifrado = self.cifrar_texto()
        print("CHAVE CIFRADA:")
        print(self.chave_cifrada)
        print("\n\nTEXTO CIFRADA:")
        print(self.texto_cifrado)

        self.escrever_arquivo("chave_cifrada.txt", self.chave_cifrada)
        self.escrever_arquivo("texto_cifrado.txt", self.texto_cifrado)

    def escrever_arquivo(self, nome, texto):
        f = open(nome, 'w+')
        f.write(str(texto))
        f.close()

    def solicitar_arquivo(self):        
        root = tk.Tk()
        root.withdraw()
        self.caminho_arquivo = filedialog.askopenfilename()

    def ler_arquivo(self):
        f = open(self.caminho_arquivo, mode="r", encoding="utf-8")
        texto = f.read()
        return texto

    def obter_chave_publica(self):
        f = open('chave_publica.txt', mode="r", encoding="utf-8")
        texto = f.read()
        return texto

    def cifrar_texto(self):
        cipher = AES.new(self.chave_byte, AES.MODE_ECB)
        texto_cifrado = cipher.encrypt(pad(self.texto_arquivo_byte, 32))
        return texto_cifrado

    def cifrar_chave(self):
        rsa = RSA.import_key(self.chave_publica)
        cipher = PKCS1_OAEP.new(rsa)
        chave_cifrada = cipher.encrypt(self.chave_byte)
        return chave_cifrada

if __name__ == "__main__":
    q = Questao02()