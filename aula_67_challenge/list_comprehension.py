string = '2987429837492834792384792384720938410893401394827348273492834'

ex1 = [string[i: i + 10] for i in range(0, len(string), 10)]
retorno = '.'.join(ex1)
print(ex1)
print(retorno)