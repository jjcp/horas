import os
import json
from datetime import datetime


class Horas(object):

    def __init__(self, ruta_hs='~/.horas.json'):
        self.ruta_hs = os.path.expanduser(ruta_hs)

    def inicio(self, nombre='horas-sueltas'):
        hs = self._leer_hs()
        self._cerrar_registros(hs)
        hs.setdefault(nombre, []).append({
            'inicio': self._hora()
        })
        self._salvar_hs(hs)

    def fin(self):
        hs = self._leer_hs()
        self._cerrar_registros(hs)
        self._salvar_hs(hs)

    def _leer_hs(self):
        return json.load(open(self.ruta_hs, 'r'))

    def _salvar_hs(self, hs):
        with open(self.ruta_hs, 'w') as f:
            f.write(json.dumps(hs, indent=4))
            f.write('\n')

    def _hora(self):
        return datetime.utcnow().isoformat()

    def _cerrar_registros(self, hs):
        for _, archivo in hs.items():
            for registro in archivo:
                if 'fin' not in registro:
                    registro['fin'] = self._hora()
