class bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando a bicicleta")
        print("Frenagem com sucesso - Bicicleta parada")

    def correr(self):
        print("Vrummmmm")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#Testando código:
b1 = bicicleta("vermelha", "caloi", 2022, 600)
print(b1)
b1.buzinar()
b1.correr()
b1.parar()
print('-'*10)
b2 = bicicleta("azul", "magrela", 2000, 200)
print(b2)
b2.correr()
b2.buzinar()
b2.parar()