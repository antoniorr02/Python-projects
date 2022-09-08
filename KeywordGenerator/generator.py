import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = [0,1,2,3,4,5,6,7,8,9]
simbolos = ['¡','!','@','#','$','%','&','/','(',')','=','*','+','?','¿','-','_','{','}']

n_words = input("¿Cuantas palabras quiere en su contraseña? ")
n_nums = input("¿Cuantos numeros quiere en su contraseña? ")
n_simbols = input("¿Cuantos simbolos quiere en su contraseña? ")

keyword = ""

for i in range(int(n_words)):
    keyword = keyword + letras[random.randint(0,len(letras)-1)]

for i in range(int(n_nums)):
    keyword = keyword + str(numeros[random.randint(0,len(numeros)-1)])

for i in range(int(n_simbols)):
    keyword = keyword + simbolos[random.randint(0,len(simbolos)-1)]

#Desordenar caracteres:
aux = list(keyword)
random.shuffle(aux)
final_keyword = ""
for i in aux:
    final_keyword = final_keyword + i 

print(final_keyword)