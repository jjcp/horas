import os
import json


class Horas(object):

    def __init__(self, ruta_hs='~/.horas.json'):
        self.ruta_hs = os.path.expanduser(ruta_hs)

    def _leer_hs(self):
        return json.load(open(self.ruta_hs, 'r'))

    def _salvar_hs(self, hs):
        with open(self.ruta_hs, 'w') as f:
            f.write(json.dumps(hs, indent=4))
            f.write('\n')
