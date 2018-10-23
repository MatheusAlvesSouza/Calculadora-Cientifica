#Calcula seno
import services.Fatorial

def seno():
	numUser = float(input("\nDigite o angulo:"))
	n = 0
	Resultado = 0
	numUser = (numUser*3.1415)/180
	for i in range(1,160,4):
		numSub = i + 2
		numPontencia = services.Fatorial.potencia(numUser,i)
		numFatorial = services.Fatorial.fatorial(i)
		numSoma = numPontencia/numFatorial
		numPontenciaSub = services.Fatorial.potencia(numUser,numSub)
		numFatorialSub = services.Fatorial.fatorial(numSub)
		numSubtracao = numPontenciaSub/numFatorialSub
		Resultado = Resultado + numSoma - numSubtracao
	print ("\nRadiano de seno = ", Resultado)

#IMPAR = +, PAR = -

if __name__ == "__main__":
	seno()