import random

res = 0
while res != 1 and res != 2:
  res = int(input("Deseja escolher o número limite?\n1 - SIM\n2 - NÃO\nEntrada: "))

limite_inferior = 1
num_escolhido = 0

if res == 2:
  limite_superior = 100
elif res == 1:
  limite_superior = 0
  while limite_superior <= limite_inferior+1:
    limite_superior = int(input("Digite o número limite: "))

num_proibido = random.randint(limite_inferior+1,limite_superior-1)
print(num_proibido)

while num_escolhido != num_proibido:
  if limite_inferior == num_proibido - 1 and limite_superior == num_proibido + 1:
    print(f'\033[32mVocê chegou nos limites e "imprensou" o número proibido ({num_proibido}).\033[0m')
    break

  num_escolhido = int(input(f"Digite um número entre {limite_inferior} e {limite_superior}: "))
  while num_escolhido >= limite_superior or num_escolhido <= limite_inferior:
    print("Número inválido!\n")
    num_escolhido = int(input(f"Digite um número entre {limite_inferior} e {limite_superior}: "))
  
  if num_escolhido != num_proibido:
    if num_escolhido > num_proibido:
      limite_superior = num_escolhido
    else:
      limite_inferior = num_escolhido
  else:
    print(f"\033[31mParabéns!!\nVocê conseguiu adivinhar o número secreto ({num_proibido})\033[0m")