import random, sys

number = random.randint(1, 10)

try:
    guess = int(input('Adivinha o número escolhido (de 1 a 10): '))

    if guess < 1 or guess > 10:
        print('Os números só vão de 1 a 10')
        sys.exit()
    
    if guess == number:
        print('Parabéns, o número está correto!')
    else:
        print(f'Número incorreto. O número correto era {number}.')

except ValueError:
    print('Por favor, insira um número válido.')