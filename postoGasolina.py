class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valor):
        """Abastece com base no valor monetário informado e retorna a quantidade de litros"""
        if valor <= 0:
            print("Erro: O valor deve ser positivo")
            return 0
            
        litros_abastecidos = valor / self.valorLitro
        
        if litros_abastecidos > self.quantidadeCombustivel:
            print(f"Erro: Não há combustível suficiente na bomba. Quantidade disponível: {self.quantidadeCombustivel:.2f} litros")
            return 0
        
        self.quantidadeCombustivel -= litros_abastecidos
        print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipoCombustivel}")
        return litros_abastecidos
    
    def abastecerPorLitro(self, litros):
        """Abastece com base nos litros informados e retorna o valor a ser pago"""
        if litros <= 0:
            print("Erro: A quantidade de litros deve ser positiva")
            return 0
            
        if litros > self.quantidadeCombustivel:
            print(f"Erro: Não há combustível suficiente na bomba. Quantidade disponível: {self.quantidadeCombustivel:.2f} litros")
            return 0
        
        valor_pagar = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        print(f"Valor a pagar: R$ {valor_pagar:.2f}")
        return valor_pagar
    
    def alterarValor(self, novo_valor):
        """Altera o valor do litro do combustível"""
        if novo_valor <= 0:
            print("Erro: O valor do litro deve ser positivo")
            return
        
        self.valorLitro = novo_valor
        print(f"Valor do litro alterado para R$ {novo_valor:.2f}")
    
    def alterarCombustivel(self, novo_tipo):
        """Altera o tipo de combustível"""
        if not novo_tipo:
            print("Erro: Tipo de combustível não pode ser vazio")
            return
        
        self.tipoCombustivel = novo_tipo
        print(f"Tipo de combustível alterado para {novo_tipo}")
    
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        """Altera a quantidade de combustível na bomba"""
        if nova_quantidade < 0:
            print("Erro: Quantidade não pode ser negativa")
            return
        
        self.quantidadeCombustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para {nova_quantidade:.2f} litros")
    
    def status(self):
        """Mostra o status atual da bomba"""
        print("\n" + "="*40)
        print(f"Tipo de combustível: {self.tipoCombustivel}")
        print(f"Valor por litro: R$ {self.valorLitro:.2f}")
        print(f"Quantidade disponível: {self.quantidadeCombustivel:.2f} litros")
        print("="*40 + "\n")


def menu():
    print("\n" + "="*40)
    print("SISTEMA DE BOMBA DE COMBUSTÍVEL")
    print("="*40)
    print("1 - Abastecer por valor")
    print("2 - Abastecer por litro")
    print("3 - Alterar valor do litro")
    print("4 - Alterar tipo de combustível")
    print("5 - Alterar quantidade de combustível")
    print("6 - Mostrar status da bomba")
    print("0 - Sair")
    print("="*40)
    
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("Erro: Digite um número válido")
        return -1


# Programa principal
if __name__ == "__main__":
    # Inicializando a bomba
    bomba = BombaCombustivel("Gasolina", 5.50, 1000)
    
    while True:
        opcao = menu()
        
        if opcao == 0:
            print("Encerrando o sistema...")
            break
            
        elif opcao == 1:  # Abastecer por valor
            try:
                valor = float(input("Digite o valor em R$ que deseja abastecer: "))
                bomba.abastecerPorValor(valor)
            except ValueError:
                print("Erro: Digite um valor numérico válido")
                
        elif opcao == 2:  # Abastecer por litro
            try:
                litros = float(input("Digite a quantidade de litros que deseja abastecer: "))
                bomba.abastecerPorLitro(litros)
            except ValueError:
                print("Erro: Digite uma quantidade numérica válida")
                
        elif opcao == 3:  # Alterar valor do litro
            try:
                novo_valor = float(input("Digite o novo valor por litro: R$ "))
                bomba.alterarValor(novo_valor)
            except ValueError:
                print("Erro: Digite um valor numérico válido")
                
        elif opcao == 4:  # Alterar tipo de combustível
            novo_tipo = input("Digite o novo tipo de combustível: ")
            bomba.alterarCombustivel(novo_tipo)
            
        elif opcao == 5:  # Alterar quantidade de combustível
            try:
                nova_quantidade = float(input("Digite a nova quantidade de combustível (litros): "))
                bomba.alterarQuantidadeCombustivel(nova_quantidade)
            except ValueError:
                print("Erro: Digite uma quantidade numérica válida")
                
        elif opcao == 6:  # Mostrar status
            bomba.status()
            
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")