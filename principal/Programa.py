


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