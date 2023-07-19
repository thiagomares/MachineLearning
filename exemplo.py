class Cadastro:
    def __init__(self, nome, sobrenome, telefone, sexo):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__telefone = telefone
        self.__sexo = sexo

    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getSexo(self):
        return self.__sexo
    
    def setSexo(self, valor):
        self.__sexo = valor
    
    def setNome(self, nome):
        self.__nome = nome
    
    def retorna_nome(self):
        return f'Olá, {self.__nome} {self.__sobrenome}'


if __name__ == "__main__":
    novo_cadastro = Cadastro('Thiago', 'mares', '31989190738', 'M')
    novo_cadastro.setNome('Vanderlucia')
    novo_cadastro.setSexo('F')
    #print(novo_cadastro.retorna_nome(), novo_cadastro.getSexo())
    
    Genius = ["Yang", "Tom", "Jerry", "Jack", "tom", "yang"]
    nomescomt = [name for name in Genius if name.startswith('T')]
    print(nomescomt) if len(nomescomt) == 1 else ...
    