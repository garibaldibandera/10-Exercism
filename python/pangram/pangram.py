def is_pangram(sentence):
    
    
    valor = True
    for char in 'abcdefghijklmnopqrstuvwxyz':
        valor = valor and (char in sentence.lower())
    return valor
