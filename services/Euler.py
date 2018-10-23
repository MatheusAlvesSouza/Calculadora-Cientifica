#Euler
import services.Fatorial

def euler():
	x = float(input("\nDigite o número para a sequência de euler:"))

	soma = 0

	for i in range(1,80,1):
		numDivSup = services.Fatorial.potencia(x,i)
		numDivSub = services.Fatorial.fatorial(i)
		r = numDivSup/numDivSub
		soma = soma + r
	print("Numero de euler = %f"%(soma+1))
if __name__ == "__main__":
	euler()