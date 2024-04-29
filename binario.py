from time import sleep
while True:
    numero = int(input("Insira um número inteiro para transformar em binário: "))
    sleep(1)
    binario = bin(n)
    if n == 0:
        print("Desligando programa")
        break
    print(f"O número {numero} em binário é {str(binario)[2:]}")
