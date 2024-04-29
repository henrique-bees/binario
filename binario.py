from time import sleep
while True:
    print("Transformador Inteiro para Binário")
    sleep(1)
    n = int(input("Insira um número inteiro: "))
    sleep(1)
    x = bin(n)
    if n == 0:
        print("Finalizando o programa!")
        break
    print(f"O número {n} em binário é {str(x)[2:]}")
