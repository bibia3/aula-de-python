import random
def main():
    notas = [0.0] * 4
    i = 0
    média = 0
    while i < 4:
        
        notas [i] = random.uniform(0, 10)

        média += notas [i]
        i += 1
    média /= 4
    print(média)
    if média >= 6:
        print("aprovado")
    elif média >= 4:
        print("recuperação")
    else:
        print("reprovado")
        
    return 0
main()
    