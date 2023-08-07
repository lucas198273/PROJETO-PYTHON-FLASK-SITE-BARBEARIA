


print('====='*20)
print('tranalhando com String : \n')
texto = "Ola mundo meu nome é lucas"
print(f"Quantidade de elementos na String = {len(texto)}")
                         
print(f"mundo no texto = {'mundo' in texto}")

print(f"Quantidade letras L no texto = {texto.count('l')}")
print(f"5 primeiras letras sao: {texto[0:10]}")

print('====='*20)
print('Trabalhando com Lista') #Lista e for
Vogais = ["e","u","s","o","u","l","u","c","a","s"]
# Item U repete com mesmo indice em todas posições
for x in Vogais:
    print(f'Posição = {Vogais.index(x)},valor = {x}')

print('====='*20)
print('Tarablhando com Lista')
print('for com enumerate: \n')
# com enumerate os indices do Item U seguem a sequencia numerica esperada (0,1,2,3,4,5,6,7,8,9)
# Utilizando a estrutura enumerate para obter índice e valor
for index, value in enumerate(Vogais):
    print(f'Posição = {index}, valor = {value}')

listaNumerica = [1,2,3,4,5,6]
print('Imprimindo lista numerica sem enumerate')
        # colocar  : apos o FOR
         
for c in listaNumerica:
    i = listaNumerica.index(c)
    print( f' Indice : { listaNumerica.index( c ) } Valor : {c}')
    print(f'Indice : {i} Valor : {c}')


print('Imprimindo lista numerica com enumerate')
                                            #value guarda a variavel enumerada
for indice , value in enumerate(listaNumerica):
    i = indice
    v = value
    print(f'indice = {indice} Valor : {value} ')
    


texto = "Meu nome é rafael sou da argentina"

palavaras = texto.split();

print(f'Palavras : {palavaras}')

vogaisMaiusculas = 'A B C D E F G H'.split()  # transforma em uma lista de elemento separados
novaLista = map(lambda x: x.lower(), vogaisMaiusculas)
novaLista = list(novaLista)
print(f'{vogaisMaiusculas}')


print('Trabalhando com range')

numeros = list(range(0,21))

print('Todos os Numeros : ',numeros)

numeroPares = list(filter(lambda x: x % 2==0,numeros))

print('Numeros Pares ',numeroPares)

numerosImpares = list(filter(lambda x: x % 2 !=0,numeros))

print('Numeros Impares ',numerosImpares)

dicionario = {'#1':1,'#2':2,'#3':3,'#4':4}
print(dicionario)

textoAleatorio = 'Meu nome é alex e estou morando na italia'

print('italia' in textoAleatorio)#retorna booleana
print('joao' in textoAleatorio) #retorna booleana

lista = [1,2,3]
valor = 4

resultado = lista.index(3) #Descobrindo indice dos elementos
print(resultado)

lista = [1,2,3]


if lista[0]<lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] =aux

if lista[1]<lista[2]:
    aux = lista[1]
    lista[1] = lista[2]
    lista[2] =aux

if lista[0]<lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] =aux
print('=====',lista)

aleatoria = [1,5,7,8,9,4]
ordenada = sorted(aleatoria)#sorted pega lista aleatoria e retorna um lista ordenada
print(ordenada)

def buscaLinear(lista,valor):
    for x in lista:
        if valor == x:
            return True
        return False

def executarBuscaBinaria(lista,valor):
    minimo =0
    maximo = len(lista)

    while minimo <= maximo:
        meio = (minimo + maximo)//2
        if valor < lista[meio]:
            maximo = meio-1
        elif valor > lista[meio]:
            minimo = meio+1
        else:
            return True
print(type(x))

objeto = Pessoa()