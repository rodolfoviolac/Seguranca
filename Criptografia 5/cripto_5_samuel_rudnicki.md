# INF01045 - Segurança Em Sistemas De Computação

## Samuel Rudnicki

## Criptografia Exercício 5

### Exercício 1

#### 1. Criptografe o texto plano indicado (M=AES is a subset of the Rijndael block cipher developed by two Belgian cryptographers, Vincent Rijmen and Joan Daemen. ) usando o template AES Cipher (Text Input) com a chave indicada (K = FD E8 F7 A9 B8 6C 3B FF 07 C0 D3 9D 04 60 5E DD).

#### Hexadecimal

>0A 18 74 93 21 95 90 D7 8A 27 1C 12 2C 85 82 C4 94 50 F6 C0 68 C4 70 1F 82 D8 04 20 0D 91 7D 16 63 16 57 AD C1 B8 7C 12 08 9B BF 18 8C 00 E1 AF 31 21 E8 9F 4E 3F BA 2F 9F 99 24 87 88 91 C0 0F 66 8E 06 8C 6C 34 5B D1 2A 66 1E 8A 36 19 8A 4B 37 FF 18 4D F9 6F F4 5E DF 93 6E CD 70 5D 70 1D 67 94 43 58 DC 99 64 A6 57 72 9F 7E 14 DD 13 B9 11 C0 71 41 38 8B C7 0A E3 84 2B 7D 2D A0 71 B3

#### Texto

>t?!????'  ,????P??h?p ??  ?} c W???|  ?? ?

#### 2. Produza as análises de frequência considerando o texto claro e o criptografado. Explique.

#### Histograma texto puro

|Caractere|Quantidade|Proporção|
|-|-|-|
A|8|0,0824742268041237
B|4|0,0412371134020619
C|4|0,0412371134020619
D|5|0,0515463917525773
E|1|:0,144329896907216
F|1|0,0103092783505155
G|2|0,0206185567010309
H|3|0,0309278350515464
I|6|0,0618556701030928
J|3|0,0309278350515464
K|1|0,0103092783505155
L|4|0,0412371134020619
M|2|0,0206185567010309
N|8|0,0824742268041237
O|6|0,0618556701030928
P|4|0,0412371134020619
R|6|0,0618556701030928
S|5|0,0515463917525773
T|5|0,0515463917525773
U|1|0,0103092783505155
V|2|0,0206185567010309
W|1|0,0103092783505155
Y|2|0,0206185567010309

#### Histograma texto criptografado

|Caractere|Quantidade|Proporção|
|-|-|-|
A|1|0,04
C|2|0,08
D|1|0,04
F|2|0,08
G|1|0,04
H|1|0,04
K|1|0,04
L|1|0,04
M|1|0,04
N|2|0,08
O|1|0,04
P|4|0,16
Q|2|0,08
R|1|0,04
T|1|0,04
W|2|0,08
X|1|0,04

>Análise de frequência para texto criptografado com AES, que faz uso dos conceitos de permutação e substituição, não faz sentido. Isto porque os bits são reordenados no processo de encriptação, perdendo-se a possibilidade de uma conversão para ASCII.

### Exercício 2

#### 1. Quebre o texto criptografado usando o template “AES Analysis using Entropy (1)”.
25 95 63 95 B6 0A A5 BA 2D 44 61 82 66 E4 32 B5 A4 8D F8 6B 9F 7C 0A B8 C1 0C 33 65 31 18 42 3D 8A 3B C9 DE C3 2C 4D
9B 43 06 78 68 7A F2 95 50 FD F6 97 98 4C C5 03 5D E4 97 BC F2 FB 91 65 AF 52 E5 E2 E3 A6 1B D8 A9 B1 E7 A8 62 52 9A FB
DD 6F FE F8 17 97 F8 EC B8 6D FB 19 69 3E B3 CB 70 59 A4 29 05 10 4F 74 E7 D2 7B 57 37 AF A2 7D EE 29 86 0F C3 0F BC 12
8F 1F 93 A4 F1 6F 90 2D 37 AB 04 B6 FD FF 3A F1 62 62 E2 8E 47 1D 70 C5 08 0F 1E 85 21 0D 98 B6 35 54 C3 D3 95 9C 3B 92
DB DC D1 66 0C B7 33 48 70 F3 FC 19 90 A8 BE EC 78 89 67 E1 1C DF 66 5C 06 E8 F1 CD 7C 63 AB 97 BB B0 B0 A1 AD B6 40
4C F1 85 A2 17 21 71 62 5E 53

>For the AES the National Institute of Standards and Technology selected three members of the Rijndael family, each with a block size of 128 bits, but three different key lengths: 128, 192 and 256 bits.

#### 2. A cifragem utilizada foi AES-128. Um caractere hex corresponde a 4 bit, assim uma chave de 128 bit pode ser descrita por 32 hex chars (32*4=128). Se (K = FF FF FF FF FF FF FF FF FF FF FF FF FF ?? ?? ??), quantos bits são desconhecidos?

>24 bits

#### 3. Configure o “Key Searcher” para FF-FF-FF-FF-FF-FF-FF-FF-FF-FF-FF-FF-FF-\*\*-\*\*-\*\*

#### 4. Mesmo ataque anterior, mas com menos bits. Configure o “Key Searcher” para FF-FF-FF-FF-FF-FF-FF-FF-FF-FF-FF-FF-F\*-\*\*-\*\*-\*\*

#### 5. Existe diferença no tempo de busca? Explique o porquê.

>Para todos os bits desconhecidos o componente KeySearcher faz uma busca exaustiva. Por serem quatro bits desconhecidos a mais na segunda configuração, espera-se que o tempo para a realização do ataque de força bruta seja de 2⁴, 16, vezes o tempo do anterior.
Na simulação realizada com a configuração de 24 bits desconhecidos, (3), o tempo para decifragem foi 20 segundos; com 28 bits desconhecidos, (4), o tempo para decifragem foi 5 minutos e 3 segundos.