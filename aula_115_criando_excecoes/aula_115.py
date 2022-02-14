class ErradoError(Exception):
    pass


def testar():
    raise ErradoError('Errado!')

testar()