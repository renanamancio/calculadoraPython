'''
nome = 'Renan Henrique'
#Comentário
print(nome)
print(nome.upper())
print(nome.lower())
print(len(nome))
print(nome[3])
print(nome.index('ri'))
print(nome.count('e'))
'''
'''
num1 = 50
num2 = 40
print(str(num1) + ' exemplo')
print(min(50, 40))
print(max(40, 50))
print(pow(4, 2))
print(round(15.49))
'''

'''
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

print('Olá ' + nome + '. ' + 'Hoje voce tem ' + idade + ' anos de idade.')
'''

'''num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
resultado = float(num1) + float(num2)

print(resultado)'''

'''amigos = ['Marcos', 'Pedro', 'Adriana', 'Karina', 'Julia']
amigos[1] = 'João'

print(amigos)'''

'''numeros = [3, 5, 12, 2, 15, 6]
amigos = ['Marcos', 'Pedro', 'Adriana', 'Karina', 'Julia']

#amigos.extend(numeros)
#amigos.append('João')
#amigos.insert(1, 'João')
#amigos.remove('Adriana')
#amigos.pop(3)
amigos.sort()
numeros.sort()

print(amigos)
print(numeros)
print(amigos.index('Pedro'))
print(amigos.count('Karina'))'''

acordei_antes9 = True
fome =  False

if acordei_antes9 and fome:
    print('Hora de fazer o café da manhã')
elif acordei_antes9 and not(fome):
    print('Hora de fazer uma corrida')
else:
    print("Hora de fazer o almoço")