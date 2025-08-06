def main() :
    num= int ( input (" Digite um numero: ") )
    divisores = ""
    i = 2
    j = 0
    while num != i and num > 1:
        if num % i == 0:
            divisores += " " + str ( i )
            j += 1
        i += 1

    if j == 0 and num > 1:
        print(" numero primo")
    elif num == 1:
        print("1 nao e primo")
    else:
        print ("nao e primo, pois e divisivel por ", j, " numeros a mais e eles sao ", divisores)
    
    
    return 0
main()  