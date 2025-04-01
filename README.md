# Documentação Formal da Aplicação: Jogo do Número Proibido

## 1. Visão Geral

Esta aplicação implementa um jogo interativo de adivinhação onde o jogador deve tentar "encurralar" um número secreto (denominado *número proibido*) sem adivinhá-lo diretamente. Durante o jogo, os limites do intervalo são ajustados dinamicamente com base nas tentativas do usuário. O programa também permite que o usuário encerre a execução digitando a letra **"q"**.

## 2. Requisitos

- **Ambiente:** Python 3.x
- **Bibliotecas Utilizadas:**
  - `random` – para geração de números aleatórios.
  - `sys` – para permitir a finalização do programa.

## 3. Funcionalidades

### 3.1. Escolha do Limite Superior
- **Descrição:**  
  O usuário decide se deseja definir manualmente o limite superior ou utilizar o valor padrão (100).
- **Processo:**  
  - Exibe um menu com as opções "SIM" (1) ou "NÃO" (2).
  - Utiliza validação para garantir que a entrada seja válida.

### 3.2. Definição dos Limites do Intervalo
- **Limite Inferior:**  
  Fixado em 1.
- **Limite Superior:**  
  - Se o usuário optar por não definir, o valor padrão será 100.
  - Caso o usuário opte por definir, o número informado deve ser maior que `limite_inferior + 1`.

### 3.3. Geração do Número Proibido
- **Descrição:**  
  O número proibido é selecionado aleatoriamente usando `random.randint()`.
- **Intervalo:**  
  Entre `limite_inferior + 1` e `limite_superior - 1` (excluindo os limites).

### 3.4. Validação e Tratamento de Entradas
- **Objetivo:**  
  Prevenir que entradas inválidas causem interrupção do programa.
- **Implementação:**  
  - Função `obter_inteiro()` centraliza a validação e inclui a opção de encerrar o programa ao digitar **"q"**.

### 3.5. Lógica do Jogo e Ajuste dos Limites
- **Mecanismo:**  
  - O usuário insere um palpite que é validado.
  - Se o palpite não for o número proibido:
    - Se o palpite for maior, o limite superior é atualizado.
    - Se for menor, o limite inferior é atualizado.
  - O jogo termina quando:
    - O usuário acerta o número proibido.
    - Os limites se estreitam a ponto de "imprensar" o número proibido (quando `limite_inferior == num_proibido - 1` e `limite_superior == num_proibido + 1`).

### 3.6. Feedback Visual
- **Uso de Cores:**  
  - Utiliza códigos ANSI para destacar mensagens (por exemplo, vermelho para acerto e verde para avisos).
- **Objetivo:**  
  Melhorar a interatividade e a experiência do usuário.

## 4. Estrutura do Código

### 4.1. Função `obter_inteiro()`

```python
import sys

def obter_inteiro(mensagem, min_val=None, max_val=None):
    """
    Solicita ao usuário que insira um número inteiro, com validação, limites opcionais e opção de sair (digitando 'q').

    Parâmetros:
      mensagem (str): Mensagem exibida para solicitar a entrada.
      min_val (int, opcional): Valor mínimo permitido (inclusive).
      max_val (int, opcional): Valor máximo permitido (inclusive).

    Retorna:
      int: Número inteiro informado pelo usuário, validado de acordo com os limites.

    Comportamento:
      - Permite ao usuário encerrar o programa ao digitar 'q' ou 'Q'.
      - Exibe mensagem de erro para entradas inválidas e solicita nova entrada.
      - Verifica se o número está dentro dos limites especificados (quando aplicável).
    """
    while True:
        entrada = input(mensagem)
        if entrada.lower() == 'q':
            print("Encerrando o programa...")
            sys.exit(0)
        try:
            valor = int(entrada)
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print("Número fora do intervalo permitido. Tente novamente.\n")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro ou 'q' para sair.\n")
```

### 4.2. Fluxo Principal do Jogo

1. **Definição do Limite Superior:**
   - O programa solicita se o usuário deseja definir manualmente o limite superior.
   - Utiliza `obter_inteiro()` para garantir a entrada válida (1 ou 2).

2. **Configuração dos Limites:**
   - `limite_inferior` é fixo em 1.
   - `limite_superior` é definido conforme a escolha do usuário (valor padrão de 100 ou valor informado pelo usuário).

3. **Geração do Número Proibido:**
   - O número proibido é gerado aleatoriamente no intervalo (`limite_inferior + 1`, `limite_superior - 1`).

4. **Loop de Adivinhação:**
   - O usuário insere palpites que são validados e utilizados para ajustar os limites.
   - A cada entrada, verifica-se se o usuário deseja encerrar o programa digitando **"q"**.
   - O jogo termina se o número for adivinhado ou se os limites se estreitarem a ponto de "imprensar" o número proibido.

5. **Encerramento:**
   - Uma mensagem final é exibida, indicando se o usuário venceu ou se os limites foram imprensados.

---

## 5. Fluxo de Execução

1. **Inicialização:**
   - O programa inicia solicitando se o usuário deseja definir o limite superior.

2. **Configuração dos Limites:**
   - Define-se `limite_inferior` como 1 e `limite_superior` conforme a escolha do usuário.

3. **Seleção do Número Proibido:**
   - Um número aleatório é gerado no intervalo definido.

4. **Interação com o Usuário:**
   - Em um loop, o usuário insere palpites, e os limites são ajustados conforme a entrada.
   - O usuário pode encerrar o programa a qualquer momento digitando **"q"**.

5. **Condição de Término:**
   - O jogo termina quando o usuário acerta o número proibido ou quando os limites se estreitam ao redor do número.

---

## 6. Considerações de Segurança e Robustez

- **Tratamento de Erros:**  
  A função `obter_inteiro()` garante que entradas inválidas não interrompam o programa.

- **Validação de Intervalos:**  
  Todas as entradas são verificadas para estarem dentro dos limites permitidos.

- **Encerramento Controlado:**  
  O usuário pode encerrar o programa de forma controlada ao digitar **"q"**.

---

## 7. Possíveis Melhorias e Extensões

- **Interface Gráfica:**  
  Implementar uma interface visual (GUI) para melhorar a experiência do usuário.

- **Modularização Avançada:**  
  Dividir o código em módulos e classes para facilitar manutenções futuras.

- **Modo Multiplayer:**  
  Permitir que vários jogadores participem alternadamente.

- **Registro de Estatísticas:**  
  Salvar pontuações e histórico de partidas para análises futuras.

---

## 8. Instruções de Uso

1. **Pré-Requisitos:**
   - Possuir o Python 3 instalado.

2. **Execução:**
   - Salve o código em um arquivo com a extensão `.py` (por exemplo, `imprensa.py`).
   - Execute o programa pelo terminal:
     ```bash
     python imprensa.py
     ```

3. **Interação:**
   - Siga as instruções exibidas na tela para definir os limites e inserir os palpites.
   - Para encerrar o programa a qualquer momento, digite **"q"**.
