try:	
	while True:
		print('By GabrielSimor')
		a = float(input('De o valor de a: '))
		b = float(input('De o valor de b: '))
		c = float(input('De o valor de c: '))
		delta = (b**2)-4*a*c
		denominador = 2*a
		raiz = delta**0.5
		numerador1 = b - raiz
		numerador2 = b + raiz
		result_x = -1*numerador1/denominador
		result_y = -1*numerador2/denominador
		print()
		if delta == 0:
			print("x' e x'' = {:.2f}".format(result_x))
			print()
		elif delta > 0:
			print("x'= {:.2f} e x''= {:.2f}".format(result_x,result_y))
			print()
		elif delta < 0:
			print('Não possui soluções reais!')
			print()
		sair = str(input('Deseja Sair? Sim ou Não:  '))
		print()
		if sair == 's' or sair == 'sim':
			break
except:
	print('isso não é um numero!')
