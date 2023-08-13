class Produto:
    def __init__(self,nome,valor,data_validade,tipo_produto) :
        self.nome = nome
        self.valor = valor
        self.data_validade = data_validade
        self.tipo_produto =tipo_produto

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Data de Validade: {self.data_validade}")
        print(f"Tipo de Produto: {self.tipo_produto}")

class Alimento(Produto):
    def __init__(self, nome, valor, data_validade, tipo_produto):
        super().__init__(nome, valor, data_validade, tipo_produto)
        self.tipo_produto = tipo_produto

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tipo de Alimento: {self.tipo_alimento}")


class Bebida(Produto):
    def __init__(self, nome, valor, data_validade, tipo_produto):
        super().__init__(nome, valor, data_validade, tipo_produto)
        self.tipo_produto = tipo_produto

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tipo de Bebida: {self.tipo_bebida}")


bebida1 = Bebida(1, "Refrigerante", 3.0, "2023-12-31", "Bebida Gaseificada")
bebida2 = Bebida(2, "Suco", 2.5, "2023-09-15", "Suco de Fruta")

alimento1 = Alimento(3, "Maçã", 1.0, "2023-08-15", "Fruta")
alimento2 = Alimento(4, "Pão", 0.5, "2023-08-10", "Pão Francês")

lista_produtos = [bebida1, bebida2, alimento1, alimento2]

for produto in lista_produtos:
    produto.exibir_informacoes()