# Exercício Python 21: Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
tempo = 10
start = str(input("Digite 'start' para começar a contagem regressiva: "))
if start == "start":
    while tempo > 0:
        print(tempo)
        tempo = (tempo - 1)
        time.sleep(1)
if tempo == 0:
    print("Fogos! 🎆🎆🎆")