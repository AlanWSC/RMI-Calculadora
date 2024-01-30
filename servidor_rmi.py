import Pyro5.api

@Pyro5.api.expose
class Calculadora:
    def adicao(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        if y == 0:
            raise ValueError('Divisão por zero não é permitida.')
        return x / y

def main():
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(Calculadora)
    ns.register('Calculadora', uri)
    print('Servidor pronto.')
    daemon.requestLoop()

if __name__ == "__main__":
    main()
