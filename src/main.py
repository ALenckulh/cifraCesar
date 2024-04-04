def criptografa(texto, indice, alfabeto):
    new_texto = ''
    for c in texto:
        index = alfabeto.find(c)
        if index == -1:
            new_texto += c
        else:
            new_index = (index + indice) % len(alfabeto)
            new_texto += alfabeto[new_index:new_index+1]
    return new_texto

def descriptografa(texto, indice, alfabeto):
    new_texto = ''
    for c in texto:
        index = alfabeto.find(c)
        if index == -1:
            new_texto += c
        else:
            new_index = (index - indice) % len(alfabeto)
            new_texto += alfabeto[new_index:new_index+1]
    return new_texto