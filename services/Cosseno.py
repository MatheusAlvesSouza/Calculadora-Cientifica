#Cosseno 
import services.Fatorial

def cosseno():
	numUser = int(input("\nDigite o angulo:"))
	n = 0
	Resultado = 0
	numUser = (numUser*3.1415)/180

	for i in range(2,160,4):
		numSub = i + 2
		numPontenciaSub = services.Fatorial.potencia(numUser,i)
		numFatorialSub = services.Fatorial.fatorial(i)
		numSubtracao = numPontenciaSub/numFatorialSub
		if i == 2:
			numSubtracao = -1*(1 - numSubtracao)
		numPontencia = services.Fatorial.potencia(numUser,numSub)
		numFatorial = services.Fatorial.fatorial(numSub)
		numSoma = numPontencia/numFatorial
		Resultado = Resultado  + numSoma -  numSubtracao
		n = n + 1
		
	print ("\nRadiano de cosseno = ", Resultado)

if __name__ == "__main__":
	cosseno()