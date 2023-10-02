#. Faca um programa que receba dois numeros e mostre qual deles ´ e o maior.

numero1= float(input("Digite aqui o primeiro valor: "))

numero2 = float(input("Digite aqui o segundo valor: "))

if numero1 > numero2:
    print("O maior número é o primeiro: ")
elif numero2 > numero1:
    print("O maior número é o segundo: ")
else:
    print("Os números são iguais.")