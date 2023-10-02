#Leia um numero fornecido pelo usu ´ ario. Se esse n ´ umero for positivo, calcule a raiz ´
#quadrada do numero. Se o n ´ umero for negativo, mostre uma mensagem dizendo que o ´
#numero ´ e inv ´ alido.

numero = float(input("Digite aqui um número: "))

if numero>=0:
    raiz_quadrada = numero **0.5
    print("A raiz quadrada desse numero é:", raiz_quadrada)
else: 
    print("O numero é invalido.")

    

