#Desafio #1

import binascii
import string
import base64

frase_1 = '-.-. --- -.. .. --. --- -- --- .-. ... . . .... ..-. .- -.-. .. .-.. -.. . .-. . -.-. --- -. .... . -.-. . .-.'
frase_2 = """41 53 43 49 49 20 63 6f 64 65 20 69 73 20 6f 6c 64 2c 20 62
75 74 20 73 74 69 6c 6c 20 77 69 64 65 6c 79 20 75 73 65 64
2e 20 48 6f 77 65 76 65 72 2c 20 74 68 65 20 6e 65 78 74 20
74 77 6f 20 70 68 72 61 73 65 73 20 61 72 65 20 6f 6c 64 65
72 20 74 68 61 6e 20 41 53 43 49 49 21"""

frase_3 = """C5 C2 C3 C4 C9 C3 40 89 A2 40 81 A2 40 96 93 84 40 81 A2 40 C1 E2 C3 C9 C9 6B 40 82 A4 A3 40 89 A3 40 89 A2 40 81 93 94 96 A2 A3 40 85 A7 A3 89 95 83 A3 4B"""

frase_4 = """10000 00001 10010 00001 10110 01010 00110 01100 10000 00001
01010 00100 01110 11000 01001 00001 00100 10011 00011 00101
00100 00111 00101 00001 01001 00100 00110 01100 00100 01110
11000 11100 11100 00111 01100 00110 01110 00011 10000 00110
11000 01100 00101 00100 11001 00001 01101 11000 01010 00001
00100 10000 10100 00001 00100 00011 01001 11110 00001 01100
10000 00100 11000 01101 00100 01110 11000 11100 10110 00111
10000 00001 01010 00101"""

frase_5 = 'QmFzZSA2NCBjYW4gYmUgdXNlZCB0byBlbmNvZGUgZS1tYWlsIGF0dGFjaG1lbnRzLg=='

frase_6 = 'WKLV LV WKH RQOB OLQH WKDW UHDOOB XVHV FUBSWRJUDSKB'

frase_7 = 'vale, et pro piscibus omnibus gratias ago'

frase_8 = "bortaS bIr jablu'DI' reH QaQqu' nay"

frase_9 = 'Perzys zaldrīzi sēnagon kostos daor'

frase_10 = """43 6f 64 65 73 20 77 69 74 68 6f 75 74 20 61 20 73 65 63
72 65 74 20 6b 65 79 20 63 61 6e 20 62 65 20 65 61 73 69 6c 79 20 64 65
63 6f 64 65 64 20 69 66 20 79 6f 75 20 6b 6e 6f 77 20 74 68 65 20 65 6e
63 6f 64 69 6e 67 20 70 72 6f 63 65 73 73 2e"""

def decifra_morse(morse_frase):
    morse_dic = {
        '.-':   'A',
        '-.':   'N',
        '-...': 'B',
        '---':  'O',
        '-.-.': 'C',
        '.--.': 'P',
        '-..':  'D',
        '--.-': 'Q',
        '.':    'E',  
        '.-.':  'R',
        '..-.': 'F',
        '...':  'S',
        '--.':  'G',
        '-':    'T',  	
        '....': 'H',
        '..-':  'U',
        '..':   'I',
        '...-': 'V',
        '.---': 'J',
        '.--':  'W',
        '-.-':  'K',
        '-..-': 'X',
        '.-..': 'L',
        '-.--': 'Y',
        '--':   'M',
        '--..': 'Z',
    }
    simbolos_frase = morse_frase.split()

    frase = ""
    for simbolo in simbolos_frase:
        frase = frase + morse_dic.get(simbolo) 

    return frase

def decifra_deslocamento(frase_deslocada):
    #cifragem c = (m+k) mod n
    possiveis_frases=[]
    alfabeto = string.ascii_uppercase

    for i in range(1,26):
        possivel_frase= ''
        for letra in frase_deslocada.upper():
            if letra in alfabeto:
                posicao = alfabeto.find(letra)
                posicao = (posicao + i) % 26
                possivel_frase = possivel_frase + alfabeto[posicao] 
        possiveis_frases.append(possivel_frase)

    return possiveis_frases

def decifra_affine(frase_cifrada, a, b):
    a_inv = {1:1,3:9,5:21,7:15,11:19,17:23,25:25}
    #cifragem c = (am +b) mod n
    alfabeto = string.ascii_uppercase
    frase_cifrada = frase_cifrada.upper()
    frase_decifrada = ''
    for letra in frase_cifrada:
        if letra in alfabeto:
            posicao_cifrada = alfabeto.find(letra)
            posicao_decifrada = a_inv[a]*(posicao_cifrada-b)%26
            frase_decifrada= frase_decifrada+alfabeto[posicao_decifrada]

    return frase_decifrada

def conta_simbolos(frase_cifrada):
    contagem_simbolos = {}

    for simbolo in frase_cifrada:
        if contagem_simbolos.get(simbolo, False) == False:
            contagem_simbolos[simbolo] = 1
        else:
            contagem_simbolos[simbolo] = contagem_simbolos.get(simbolo)+1

    return contagem_simbolos
#frase 1
print("Frase 1: " + frase_1)
print('Decodificacao: ' + decifra_morse(frase_1))

#frase 2
print("Frase 2: " + frase_2)
print('Decodificacao: ' + str(binascii.unhexlify(''.join(frase_2.split()))))        

#frase 3
#EBCDIC
print("Frase 3: "+ frase_3)
frase_3 = ''.join(frase_3.split())
frase_3 = bytes(int(frase_3[i:i+2], 16) for i in range(0, len(frase_3),2))
print("Decodificacao: "+ frase_3.decode("cp500"))
    
#frase 4
print('Frase 4: ' + frase_4)


#frase 5
print("Frase 5: "+ frase_5)
print("Decodificacao: "+ str(base64.b64decode(frase_5)))

#frase 6
print("Frase 6: "+ frase_6)
#print(decifra_deslocamento(frase_6))
print('Decodificação: '+ 'THIS IS THE ONLY LINE THAT REALLY USES CRYPTOGRAPHY')

#frase 7
print("Frase 7: "+ frase_7)
print(sorted(conta_simbolos(frase_7), key= conta_simbolos(frase_7).get, reverse=True))
print(conta_simbolos(frase_7))

#frase 8
print("Frase 8: "+ frase_8)
print(sorted(conta_simbolos(frase_8), key= conta_simbolos(frase_8).get, reverse=True))
print((conta_simbolos(frase_8)))
print(decifra_affine(frase_8, 7,24))

#frase 9
print("Frase 9: "+ frase_9)
print(sorted(conta_simbolos(frase_9), key= conta_simbolos(frase_9).get, reverse=True))

#frase 10
print('Frase 10: ' + str(binascii.unhexlify(''.join(frase_10.split()))))