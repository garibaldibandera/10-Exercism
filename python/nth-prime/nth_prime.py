from math import sqrt



def prime(number):
    if number < 1:
        raise ValueError("El número de primos debe ser mayor que cero")
    lista = [2]
    p = 3
    while len(lista) < number:
        if primo(p):
            lista.append(p)
        p += 2
    return lista[number -1]     
                    
        
def primo(numero):
    for i in range(2, round(sqrt(numero) + 1)):
        if numero % i == 0:
            return False
    return True
               