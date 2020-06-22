objetivo = int(input('Escoje un numero : \n'))
epsilon = 0.1
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
  respuesta += paso
if abs(respuesta**2 - objetivo) >= epsilon:
  print(f'No se encontr[o la ra[iz cuadrada de {objetivo}')
else:
  print(f'La raiz cuadrada de {objetivo} es {respuesta}')