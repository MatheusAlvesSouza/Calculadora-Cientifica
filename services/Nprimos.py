#Calcula numeros primos
def Nprimos():
	n = int(input('Digite um inteiro > 1: '))
	ref = 0
	while n<=0:
		n = int(input('Digite um inteiro > 1: '))
	for i in range(2, n//2+1, 1):
		if not n % i:			
			if ref == 0:
				print('\n%d não é um nº primo pois é divisível por:\n' % n)
				ref = 1
			print('%d ' % i, end='')

	if ref == 0:
		print('\n%d é um nº primo.\n' % n)

	print('\n')
if __name__ == "__main__":
	Nprimos()