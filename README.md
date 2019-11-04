# Desenvolvimento de Sistemas Seguros - Exercício 08

Fundação da Universidade Regional de Blumenau

Alunos: 
* Francisco Lucas Sens
* Gabriel Castellani de Oliveira

[Conteúdo](assets/15-CriptografiaDeChavePública.pdf)

# Enunciado: 

Publique as soluções no AVA e salve os resultados num documento no Word, conforme indicado em cada questão.

## Questão 1
Crie um programa que gere um par de chaves privada e pública relacionadas.

Exiba o valor do módulo e dos expoentes de cada chave gerada.

Salve cada uma das chaves num arquivo separado, pois as chaves precisarão ser recuperadas nas questões seguintes.

Num documento do Word, coloque o expoente da chave pública, da chave privada e o módulo do par de chaves gerados.

### Resposta: 
* Expoente chave pública:  65537 
* Módulo chave privada: 135308873914195696393338484616246635058026472634569733152551239970101179358439522334575854846557168797856536521570448460229692158098690911132128323884576577686567612403423813147670867207074182711585791971782078684680636860231424181002533683618314987430994135535014847273047801459094213321796166850724371486819
* Expoente chave privada: 65537
* Módulo chave pública: 47750486532607810338970848104193847378153352443540729486430643423234204742389631392252778901859624333686710967405913178634852377016136280157222086375673078563604766438668714414242987675889497780556435541743499119880691635234131190664479161291156789578140089537175379996824881031561070808075457892221098409793

## Questão 2

Crie um programa que criptografe um arquivo submetido pelo usuário utilizando o algoritmo AES.

Criptografe a chave simétrica (do algoritmo AES) utilizando a chave pública gerada na questão 1.

Num documento do Word, coloque o texto simples, bem como o texto cifrado pelo algoritmo RSA.

### Resposta: 
* Texto simples: Hello Darkness asdasndosan doaosn doansd onaosn as
* Texto cifrado: b'.N,v\xc6B2\x1d\xba\xd4\xb1\xa37\xed\xb1\x83\xae\xa6h,\x0b\xbf=\x13NP>d\x1d\xac\xea\x19f\x83\r\xa9+\xf9\x9c\x12[\xbf\xeb\n(qQ\xe2J\xda\xcc\xb5\xa4\x9d\xddoS\x86\xf1\xe8\x0e\x9e\xefY'

## Questão 3

Crie um programa que decriptografe a chave de um algoritmo AES, utilizando a chave assimétrica privada gerada na questão 1.

Decriptografe o arquivo utilizando a chave obtida.