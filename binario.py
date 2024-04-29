while True:
    print("Transformador Inteiro para Binário")
    n = int(input("Insira um número inteiro: "))
    x = bin(n)
    if n == 0:
        print("Finalizando o programa!")
        break
    print(f"O número {n} em binário é {str(x)[2:]}")
