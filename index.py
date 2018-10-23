#menu
import os

import services.QtdNprimos
import services.Fibonacci
import services.Nprimos
import services.Seno
import services.Cosseno
import services.Euler

from moldura import moldura

os.system("cls")

def menu():
	print("\n1.Sêquencia Fibonacci")
	print("2.Verificação de número primo")
	print("3.Sêquencia de números primos")
	print("4.Sen(x)")
	print("5.Cos(x)")
	print("6.e×")
	print("7.Limpar a tela")
	print("8.Sair")

	op = int(input("\nOpção:"))
	
	if op == 1:
		services.Fibonacci.fibonacci()
	elif op == 2:
		services.Nprimos.Nprimos()
	elif op == 3:
		services.QtdNprimos.QtdNprimos()
	elif op == 4:
		services.Seno.seno()
	elif op == 5:
		services.Cosseno.cosseno()
	elif op == 6:
		services.Euler.euler()
	elif op == 7:
		os.system("cls")
	elif op == 8:
		os.system("cls")
		exit()
	else:
		os.system("cls")
		print("***Valor inválido***")

while True:
	try:
		print('\n')
		moldura("Calculadora científica")
		menu()

	except ValueError:
		os.system("cls")
		print("***Valor inválido***")
	except Exception as erro:
		print("Erro inesperado")