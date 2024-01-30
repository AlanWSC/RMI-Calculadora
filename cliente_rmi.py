import Pyro5.api

def main():
    uri = 'PYRONAME:Calculadora'
    with Pyro5.api.Proxy(uri) as calculadora:
        while True:
            print('Escolha uma operação:')
            print('1 - Adição')
            print('2 - Subtração')
            print('3 - Multiplicação')
            print('4 - Divisão')
            print('5 - Sair')

            escolha = input('Digite o número da operação desejada: ')
            if escolha == '5':
                break

            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))

            if escolha == '1':
                resultado = calculadora.adicao(num1, num2)
            elif escolha == '2':
                resultado = calculadora.subtracao(num1, num2)
            elif escolha == '3':
                resultado = calculadora.multiplicacao(num1, num2)
            elif escolha == '4':
                resultado = calculadora.divisao(num1, num2)
            else:
                print('Escolha inválida.')
                continue

            print(f'Resultado: {resultado}')

if __name__ == "__main__":
    main()
