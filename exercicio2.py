
def duplicados(array):
    novoArray = []
    for palavra in array: 

        chars = []
        anterior = None
 
        for char in palavra:
            if anterior != char:
                chars.append(char)
                anterior = char
 
        novoArray.append(''.join(chars))
    return novoArray


print(duplicados(["abracadabra","allottee","assessee"]))
print(duplicados(["kelless","keenness","Alfalggo"]))

