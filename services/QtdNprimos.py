#Calcula numeros primos
def QtdNprimos():
	qtd = int(input('\nQuantidade de nºs primos? '))
	print('\r')

	while qtd<=0:
		qtd = int(input('\nQuantidade de nºs primos? '))
	count = 0
	num = 2

	while count < qtd: 
		ref = 0
		for i in range(2, num//2+1, 1):
			if not num % i:
				ref = 1	
				break
		
		if ref == 0:
			print('%d' % num, end=', ' if count != qtd -1 else '')
			count += 1
		num += 1
	print('\r')

if __name__ == "__main__":
	QtdNprimos()
