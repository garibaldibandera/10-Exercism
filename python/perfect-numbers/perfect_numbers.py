def classify(number):
    
    
    if number < 1:
        raise ValueError('Número ingresado debe ser mayor que 0')
    sumatoria = sum([i for i in range(1, number//2+1) if number% i==0])
    if sumatoria == number:
        return 'perfect'
    elif sumatoria > number:
        return 'abundante'
    elif sumatoria < number:
        return 'deficient'
