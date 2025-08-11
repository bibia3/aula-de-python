from Soma import soma
from Div import div
from Mult import mult 
from Sub import sub

def main():

    num1 = int (input("Digite o primeiro numero: "))
    num2 = int (input("Digite o segundo numero: "))

    print("A soma de ", num1, " + ", num2, " = ", soma(num1,num2))
    print("A subtraçao de", num1, "-", num2, " = ", sub(num1, num2))
    print("A multiplicaçao de ", num1, " * ", num2, " = ", mult(num1, num2))
    print("A divisao de", num1, " / ", num2, " = ", div (num1, num2)) 
    return 0
main()