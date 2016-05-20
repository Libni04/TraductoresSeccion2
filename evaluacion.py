import re

def ValidaTecla(tecla):
	if re.search('[a-z], tecla'):
		return 'Solo se requiere letras'
	elif tecla.isalnum(tecla):
		return 'Solo se requiere letras y numeros'
	else:
		return 'Caracteres aceptados'

teclado = raw_input('Ingrese los Caracteres')
print ValidaTecla(teclado)