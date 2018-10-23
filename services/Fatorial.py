#FATORIAL e POTÊNCIA
def fatorial(n):   
    f = n
    for i in range(1,n,1):
        f = f * i
    return f

def potencia(numUser, numMaq):
	n = numUser**numMaq
	return n

if __name__ == "__main__":
	n = int(input("Digite um numero para o fatorial:"))
	r = fatorial(n)
	print("Fatorial de %2.f é igual a: " %n, r)