from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida
from MotoristaDAO import MotoristaDAO

class MotoristaCLI:
    def __init__(self, motorista_model):
        self.motorista_model = motorista_model

    def criar_motorista(self):
        corridas = []
        while True:
            nome = input("Digite o nome do passageiro: ")
            documento = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)

            notaCorrida = int(input("Digite a avaliação da corrida: "))
            distancia = float(input("Digite a distância da corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(notaCorrida, distancia, valor, passageiro)
            corridas.append(corrida)

            aux = input("Deseja adicionar outra corrida para este motorista? (s/n): ")
            if aux.lower() == 'n':
                break

        notaMotorista = int(input("Digite a avaliação do motorista: "))
        motorista = Motorista(notaMotorista, corridas)
        self.motorista_model.criar_motorista(motorista)

    def ler_motorista(self):
        id = input("Digite o ID: ")
        motorista = self.motorista_model.ler_motorista(id)

        if motorista:
            print(f'Avaliação do motorista: {motorista.notaMotorista}')
            for corrida in motorista.corridas:
                print(f'Avaliação da corrida: {corrida.notaCorrida}')
                print(f'Distância da corrida: {corrida.distancia}')
                print(f'Valor da corrida: {corrida.valor}')
                print(f'Nome do passageiro: {corrida.passageiro.nome}')
                print(f'Documento do passageiro: {corrida.passageiro.documento}')
        else:
            print(f'Motorista não encontrado com o ID: {id}')

    def atualizar_motorista(self):
        id = input("Digite o ID: ")
        corridas = []
        while True:
            nome = input("Digite o nome do passageiro: ")
            documento = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)

            notaCorrida = int(input("Digite a avaliação da corrida: "))
            distancia = float(input("Digite a distância da corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(notaCorrida, distancia, valor, passageiro)
            corridas.append(corrida)

            aux = input("Deseja adicionar outra corrida para este motorista? (s/n): ")
            if aux.lower() == 'n':
                break

        notaMotorista = int(input("Digite a avaliação do motorista: "))
        motorista = Motorista(notaMotorista, corridas)
        updated_count = self.motorista_model.atualizar_motorista(id, motorista)

        if updated_count > 0:
            print(f'Motorista atualizado: {updated_count} documentos atualizados')
        else:
            print(f'Motorista não encontrado com o id: {id}')

    def excluir_motorista(self):
        id = input("Digite o ID: ")
        deleted_count = self.motorista_model.excluir_motorista(id)

        if deleted_count > 0:
            print(f'Motorista deletado: {deleted_count} documentos deletados')
        else:
            print(f'Motorista nao encontrado com o id: {id}')
    def run(self):
        while True:
            print("Menu:")
            print("1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Excluir Motorista")
            print("5. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.criar_motorista()
            elif choice == "2":
                self.ler_motorista()
            elif choice == "3":
                self.atualizar_motorista()
            elif choice == "4":
                self.excluir_motorista()
            elif choice == "5":
                print("Tchau!")
                break
            else:
                print("Opção inválida. Tente novamente.")