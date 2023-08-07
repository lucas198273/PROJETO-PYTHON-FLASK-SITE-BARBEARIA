

class Televisao():
    print('Televisao Ligada')
    
    def __init__(self):
        self.volume = 10 #Instancia variavel dentro do construtor com valor definido
        # self.televisao_Ligada = False
    def aumenta_volume(self):
        self.volume += 1
    def reduz_volume(self):
        self.volume -= 1

    # def botao_ligar_desligar(self):
    #     if self.televisao_Ligada == False:
    #         self.televisao_Ligada == True
    #     else pri

tv = Televisao()
print('Volume inicial ', tv.volume)
tv.aumenta_volume()        #Nao Esquecer do parenteses
tv.aumenta_volume()        ## Nao esquecer o parenteses apos a chamada da função função
print('Volume Atual ',tv.volume)


class ContaCorrente:          # apos o nome da função colocar : 
    def __init__(self):      # (self) padrao nos metodos
        self.saldo = 1500
    def depositar(self,valor):   
        self.saldo += valor
    def sacar(self , valor):   
        self.saldo -= valor
    def get_saldo(self):
        return self.saldo


c = ContaCorrente()
c.depositar(500)
c.sacar(500)
print("\n\n   saldo :",c.get_saldo(),"\n =================")






class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}"
    # classeFilha(ClasseMae)

class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)  # Chama o construtor da classe base
        self.curso = curso

    def cumprimentar(self):
        return f"Oi, eu sou {self.nome} e estudo {self.curso}"

class Funcionario(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome) # aponta a variavel para o construtor da classe mae
        self.salario = salario

    #   self cria variavel = parametro    
    def consulta_salario(self):         # Usar self para apontar a variavel
        return self.salario
    def cumprimentar(self):
        return f"Oi, eu sou {self.nome} e estudo {self.salario}"

    
estudante1 = Estudante("João","Programação")
estudante2 = Estudante("Maria", "Medicina")
funcionario1 = Funcionario("Lucas",1500)
funcionario2= Funcionario("Guilherme",1500)
funcionario3 = Funcionario("Guilherme",1500)

lista_pessoas = [estudante1,estudante2,funcionario1,funcionario2,funcionario3]


for pessoa in lista_pessoas:
    if isinstance(pessoa, Funcionario):
        print(f"Funcionário: {pessoa.nome}, Salário: {pessoa.consulta_salario()}")
    elif isinstance(pessoa, Estudante):
        print(f"Estudante: {pessoa.nome}, Curso: {pessoa.curso}")