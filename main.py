from database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

motoristaDAO = MotoristaDAO(database= Database(database="exercicio_avaliativo_1", collection="Motoristas"))

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()
