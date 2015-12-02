import os


class Horas(object):

    def __init__(self, ruta_hs='~/.horas.json'):
        self.ruta_hs = os.path.expanduser(ruta_hs)
