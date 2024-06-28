# Retorna os X primeiros numeros da sequência
def fibonacci(qtt:int):
    sequence = [0,1]

    i = 2

    while i < qtt:
       sequence.append(sequence[i-1] + sequence[i-2])
       i += 1


    return sequence