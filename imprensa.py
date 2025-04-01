import random
import sys

print(f"\033[93mATENÇÂO!!!!!\nSe desejar sair digite 'q'.\n\033[0m")

def obter_inteiro(mensagem, min_valor=None, max_valor=None):
  while True:
    entrada = input(mensagem)
    # Verifica se o usuário deseja encerrar o programa
    if entrada.lower() == 'q':
        print("\033[93mEncerrando o programa...\033[0m")
        sys.exit(0)
    try:
      valor = int(entrada)
      if (min_valor is not None and valor < min_valor) or (max_valor is not None and valor > max_valor):
        print("\033[93mNúmero fora do intervalo permitido.\nTente novamente\033[0m!")
      else:
        return valor
    except ValueError:
      print("\033[93mEntrada inválida. Por favor, digite um número inteiro.\n\033[0m")

res = 0
while res != 1 and res != 2:
  res = obter_inteiro("Deseja escolher o número limite?\n1 - SIM\n2 - NÃO\nEntrada: ", min_valor=1, max_valor=2)

limite_inferior = 1
num_escolhido = 0

if res == 2:
  limite_superior = 100
elif res == 1:
  limite_superior = 0
  while limite_superior <= limite_inferior+1:
    limite_superior = obter_inteiro("\nDigite o número limite: ", min_valor= limite_inferior+2)

num_proibido = random.randint(limite_inferior+1,limite_superior-1)

while num_escolhido != num_proibido:
  if limite_inferior == num_proibido - 1 and limite_superior == num_proibido + 1:
    print(f'\033[32mVocê chegou nos limites e "imprensou" o número proibido ({num_proibido}).\033[0m')
    break

  num_escolhido = obter_inteiro(f"\nDigite um número entre {limite_inferior} e {limite_superior}: ", min_valor=limite_inferior+1, max_valor=limite_superior-1)
  
  if num_escolhido != num_proibido:
    if num_escolhido > num_proibido:
      limite_superior = num_escolhido
    else:
      limite_inferior = num_escolhido
  else:
    print(f"\033[31mParabéns!! (IRONIA)\nVocê digitou o número proibido ({num_proibido})\033[0m")