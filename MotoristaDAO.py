from pymongo import MongoClient
from bson.objectid import ObjectId
from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida

class MotoristaDAO:
    def __init__(self, database):
        self.db = database.collection

    def criar_motorista(self, motorista):
        try:
            motorista_dict = {
                "notaMotorista": motorista.notaMotorista,
                "corridas": self._parse_corridas(motorista.corridas),
            }
            res = self.db.insert_one(motorista_dict)
            inserted_id = str(res.inserted_id)
            print(f"Motorista criado com o id: {inserted_id}")
            return inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def ler_motorista(self, motorista_id):
        try:
            motorista_dict = self.db.find_one({"_id": ObjectId(motorista_id)})
            if not motorista_dict:
                print(f"Motorista não encontrado com o id: {motorista_id}")
                return None

            motorista = Motorista(
                motorista_dict["notaMotorista"],
                self._parse_corridas_dict(motorista_dict["corridas"])
            )
            print(f"Motorista encontrado: {motorista_dict}")
            return motorista
        except Exception as e:
            print(f"Ocorreu um erro ao ler o motorista: {e}")
            return None

    def atualizar_motorista(self, motorista_id, motorista):
        try:
            motorista_dict = {
                "notaMotorista": motorista.notaMotorista,
                "corridas": self._parse_corridas(motorista.corridas),
            }
            res = self.db.update_one(
                {"_id": ObjectId(motorista_id)},
                {"$set": motorista_dict}
            )
            if res.modified_count == 0:
                print(f"Motorista não encontrado com o ID: {motorista_id}")
            else:
                print(f"Motorista atualizado: {res.modified_count} documentos atualizados")
            return res.modified_count
        except Exception as e:
            print(f"Um erro ocorreu ao atualizar o motorista: {e}")
            return None

    def excluir_motorista(self, motorista_id):
        try:
            res = self.db.delete_one({"_id": ObjectId(motorista_id)})
            if res.deleted_count == 0:
                print(f"Motorista não encontrado com o id: {motorista_id}")
            else:
                print(f"Motorista deletado: {res.deleted_count} documentos deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Um erro ocorreu ao deletar o motorista: {e}")
            return None

    def _parse_corridas(self, corridas):
        return [
            {
                "notaCorrida": corrida.notaCorrida,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento,
                },
            }
            for corrida in corridas
        ]

    def _parse_corridas_dict(self, corridas_dict):
        return [
            Corrida(
                corrida["notaCorrida"],
                corrida["distancia"],
                corrida["valor"],
                Passageiro(
                    corrida["passageiro"]["nome"],
                    corrida["passageiro"]["documento"]
                )
            )
            for corrida in corridas_dict
        ]
