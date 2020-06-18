def sum_of_multiples(limit, multiples):
    
    
    suma = 0
    multiples = [item for item in multiples if item != 0]

    for numero in range(1, limit):
        if [item for item in multiples if numero % item == 0]:
            suma += numero

    return suma
