#Fac¸a um programa que leia um numero e, caso ele seja positivo, calcule e mostre: ´
#• O numero digitado ao quadrado ´
#• A raiz quadrada do numero digitado

numero = float(input("Digite aqui seu numero: "))

if numero >=0:
    quadrado = numero*numero
print("O número ao quadrado é",quadrado)

raiz_quadrada = numero **0.5

print("a raiz quadrada desse número é",raiz_quadrada)


