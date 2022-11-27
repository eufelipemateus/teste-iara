numero = None
total = 0
somaTexto = None

while(numero is None):
    numero = int(input("Digite um numero: "))
    if numero <= 0 :
        print("Numero precisa maior que 0.")
        numero = None
    if numero >= 100000:
        print("Numero precisa menor igual á 100000.")
        numero = None

for i in range(1,numero+1):
    if somaTexto != None:
        somaTexto += "+"
    else:
        somaTexto = ''
    somaTexto += '{}'.format(i)
    total += i

print("-------------------------")
print ("Soma({})-> {} ({})".format(numero, total,somaTexto)) 


