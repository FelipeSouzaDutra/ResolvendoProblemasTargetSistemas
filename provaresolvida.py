
# Exercicio relacido a fibonacci
def fibonacci(tamanho):
    fibonaccis = [0, 1]  # Inicializa a lista com os dois primeiros números da sequência
    while len(fibonaccis) < tamanho:
        proximo = fibonaccis[-1] + fibonaccis[-2]  # Calcula o próximo número da sequência
        fibonaccis.append(proximo)  # Adiciona o próximo número
    return fibonaccis


print('Informe o tamanho da sequencia de fibonnaci: ')
tamanho: int = int(input())
fibonaccis = fibonacci(tamanho)
print('Informe o numero que vc deseja encontrar na sequencia: ')
numero: int = int(input())

if numero in fibonaccis:
    print(f'O número {numero} está na lista.')
else:
    print(f'O número {numero} não está na lista.')

#Exercicio relacionado a string :

print('=========================================================')
print('Exercicio 5:')

nome: str = 'prova'
print(nome)
novo_nome: str = ''
for palavra in nome:
    novo_nome = palavra + novo_nome
print(f'Invertando a palavra acima teremos :{novo_nome} ')