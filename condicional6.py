#Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, ´
#assim como a diferenc¸a existente entre ambos.

numero1 = int(input("Digite aqui o primeiro numero: "))

numero2 = int(input("Digite aqui o segundo numero: "))

if numero1 > numero2:
    maior_numero = numero1
else:
    maior_numero = numero2

diferenca = abs(numero1 - numero2)


print(f"O maior número é: {maior_numero}")
print(f"A diferença entre os números é: {diferenca}")