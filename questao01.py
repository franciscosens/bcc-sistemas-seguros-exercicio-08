from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
from collections import namedtuple

class GerarChaves:
    
    def __init__(self):
        keys = self.newkeys(1024)
        chave_publica = keys.public.export_key().decode()
        self.escrever_arquivo('chave_publica.txt', chave_publica)

        chave_privada = keys.private.export_key().decode()
        self.escrever_arquivo('chave_privada.txt', chave_privada)

    def escrever_arquivo(self, nome, texto):
        f = open(nome, 'w+')
        f.write(str(texto))
        f.close()

    def newkeys(self, keysize):
        random_generator = Random.new().read
        key = RSA.generate(keysize, random_generator)
        retorno = namedtuple("private", "public")
        retorno.public = key.publickey()
        retorno.private = key
        return retorno

if __name__ == "__main__":
    conversor = GerarChaves()