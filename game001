import random
import time

print('Bem vindo ao Game de Adivinhação!')

palavras = ['macaco','peixe','zebra','cavalo','rinoceronte','girafa','hipopotamo', 'penguim']
palavra_misteriosa = random.choice(palavras)
digitadas = []
vidas = 3
letras_na_palavra = len(palavra_misteriosa)
print('A palavra secreta possui {} letras e é um animal!'.format(letras_na_palavra))
while True:
	if vidas == 0:
		print('Você perdeu, a palavra era {}'.format(palavra_misteriosa))
		time.sleep(3)
		break		
	letra = str(input('Digite uma letra: '))
	if letra == 'sair':
		break
	if len(letra)> 1:
		print('Digite apenas uma letra!')
		continue
	if len(letra) == 0:
		print('Digite alguma coisa!')
		continue
	if letra == 'sair':
		break
	digitadas.append(letra)

	if letra in palavra_misteriosa:
		print('Você acertou!')
	if letra not in palavra_misteriosa:
		vidas = vidas - 1 
		print('Você errou, tem {}'.format(vidas))
		digitadas.pop()

	temporario = ''
	for letra_secreta in palavra_misteriosa:
		if letra_secreta in digitadas:
			temporario += letra_secreta
		else:
			temporario += '*'

	if temporario == palavra_misteriosa:
		print('Parabens você acertou, a palavra era {}'.format(palavra_misteriosa))
		time.sleep(3)
		break
	print(temporario)






