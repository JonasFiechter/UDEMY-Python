from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor1 = Escritor('José')
escritor2 = Escritor('Marcus')
caneta1 = Caneta('Bic')
maquina1 = MaquinaDeEscrever()

escritor1.ferramenta = caneta1
escritor2.ferramenta = maquina1
escritor1.ferramenta.escrever()
escritor2.ferramenta.escrever()

del escritor1